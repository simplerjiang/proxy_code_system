from django.shortcuts import render
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse #用来进行命名空间的反调用
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse,HttpResponseRedirect #HttpResponseRedirect是用于进行url进行跳转
from main_app.models import *
from datetime import date,timedelta
from .time_deal import *
from django.contrib.auth.decorators import login_required
import django.utils.timezone as timezone
from django.http import Http404
from decimal import *


def make_auth(request):
    if request.method == "GET":
        return render(request,"make-auth.html")
    elif request.method == "POST":
        software_code = request.POST['software_code']
        customer_QQ = request.POST['customer_QQ']
        bot_QQ = request.POST['bot_QQ']
        if software_code == '' or customer_QQ == '' or bot_QQ == '':
            context ={"warn":"请填写完整信息","software_code":software_code,"customer_QQ":customer_QQ,"bot_QQ":bot_QQ}
            return render(request,"make-auth.html",context)
        try:
            customer_QQ = int(customer_QQ)
            bot_QQ = int(bot_QQ)
        except:
            context = {"warn": "请填写正确的QQ", "software_code": software_code}
            return render(request,"make-auth.html",context)

        try:
            code_object = Time_code.objects.get(code=software_code)
        except Time_code.DoesNotExist:
            context = {"warn": "卡密错误！请重试！", "software_code": software_code, "customer_QQ": customer_QQ, "bot_QQ": bot_QQ}
            return render(request, "make-auth.html", context)
        if code_object.used == True:
            context = {"warn": "卡密已失效！请重试！", "software_code": software_code, "customer_QQ": customer_QQ,
                       "bot_QQ": bot_QQ}
            return render(request,"make-auth.html",context)

        software = code_object.software
        time_long = code_object.time
        proxy_man = code_object.proxy_man


        try:
            authorization = Authorization.objects.get(software=software, bot_QQ=bot_QQ)
            #如果不存在，这里会爆炸
            if authorization.deadline_time < timezone.now(): #如果存在，且时间小于现在，说明已经过期了
                authorization.deadline_time = datetime.datetime.now() #设定时间为现在
                authorization.save()

            authorization.customer_QQ = customer_QQ #再重新设立主人id,以防止某些查询的时候遇到试用授权的
            authorization.deadline_time = authorization.deadline_time + datetime.timedelta(hours=time_long)
            authorization.proxy_man = proxy_man
            authorization.save()
            code_object.used = True
            code_object.save()

            context = {"success":"已创建授权，到期时间："+ convert_timezone(authorization.deadline_time).strftime("%Y-%m-%d %H:%M:%S")}
            return render(request,"make-auth.html",context)
        except Authorization.DoesNotExist:  # 如果授权不存在，新创立
            authorization = Authorization.objects.create(software=software,
                                                         customer_QQ=customer_QQ,
                                                         proxy_man=code_object.proxy_man,
                                                         bot_QQ=bot_QQ,
                                                         )
            authorization.save()
            authorization.deadline_time = authorization.deadline_time + datetime.timedelta(hours=time_long)
            authorization.save()
            code_object.used = True
            code_object.save()

            context = {
                "success": "已续费授权，到期时间：" + convert_timezone(authorization.deadline_time).strftime("%Y-%m-%d %H:%M:%S")}
            return render(request, "make-auth.html", context)


def change_bot_qq(request):
    if request.method == "GET":
        software_list = Software.objects.all()
        context = {"software_list":software_list}
        return render(request,"change-auth.html",context)

    elif request.method == "POST":
        software_list = Software.objects.all()
        software_id = request.POST['software_id']
        customer_QQ = request.POST['customer_QQ']
        obot_QQ = request.POST['obot_QQ']
        bot_QQ = request.POST['bot_QQ']
        if software_id == 0:
            context ={"warn":"暂时没有可用软件！请联系管理员","software_list":software_list,"customer_QQ":customer_QQ,"obot_QQ":obot_QQ,"bot_QQ":bot_QQ}
            return render(request,"change-auth.html",context)

        if customer_QQ == '' or obot_QQ == '' or bot_QQ == '':
            context ={"warn":"请填写完整的信息！","software_list":software_list,"customer_QQ":customer_QQ,"obot_QQ":obot_QQ,"bot_QQ":bot_QQ}
            return render(request,"change-auth.html",context)

        try:
            customer_QQ = int(customer_QQ)
            obot_QQ = int(obot_QQ)
            bot_QQ = int(bot_QQ)

        except:
            context = {"warn":"请输入正确的QQ号","software_list":software_list}
            return render(request,"change-auth.html",context)
        try:
            software = Software.objects.get(software_id=software_id)
        except Software.DoesNotExist:
            raise Http404("404")

        try:
            auth_object = Authorization.objects.get(customer_QQ=customer_QQ,bot_QQ=obot_QQ,software=software)

        except Authorization.DoesNotExist:
            context ={"warn":"没有找到匹配的授权信息！请重试","software_list":software_list,"customer_QQ":customer_QQ,"obot_QQ":obot_QQ,"bot_QQ":bot_QQ}
            return render(request,"change-auth.html",context)

        if auth_object.bot_QQ == bot_QQ:
            context ={"warn":"新旧机器人QQ相同！请重试","software_list":software_list,"customer_QQ":customer_QQ,"obot_QQ":obot_QQ,"bot_QQ":bot_QQ}
            return render(request,"change-auth.html",context)

        try:
            Authorization.objects.get(bot_QQ=bot_QQ,software=software)
            context ={"warn":"新的机器人QQ已经存在，请尝试其他Q号或联系管理员","software_list":software_list,"customer_QQ":customer_QQ,"obot_QQ":obot_QQ,"bot_QQ":bot_QQ}
            return render(request,"change-auth.html",context)
        except Authorization.DoesNotExist:
            auth_object.bot_QQ == bot_QQ
            auth_object.save()
            context = {"success": "修改成功！新的机器人QQ号为："+str(bot_QQ), "software_list": software_list}
            return render(request, "change-auth.html", context)



