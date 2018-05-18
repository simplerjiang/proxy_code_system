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


def web_test(request):
    return render(request,"table-datatable.html")

@login_required
def index_page(request): #控制台主页
    user = request.user
    context = {"username":user.username}
    try:
        user_other_info = Others_info.objects.get(user=user)
    except:
        return HttpResponse("出现错误！报告错误号：1000。\n 你可能登陆了多个账户或管理员账户，请登出后再操作！")
    context["money"] = user_other_info.balance

    try:  #查找授权
        auths = Authorization.objects.filter(proxy_man=user).order_by('id')
        context["auths_num"] = len(auths)
        auths_list =[]
        auths = auths.reverse()
        for i in auths[:4]:
            a = {"auths_software":i.software,"auths_cust":i.customer_QQ}
            a["auths_begin_time"] = i.begin_time.strftime("%Y-%m-%d")
            auths_list.append(a)
            if i.deadline_time < timezone.now():
                a["auths_state"] = False
            else:
                a["auths_state"] = True
        context["auths_list"] = auths_list
    except:
        context["auths_num"] = 0

    try:
        software_num = Software.objects.all()
        context["software_num"] = len(software_num)
    except:
        context["software_num"] = 0
    try:
        proxy_man_num = User.objects.all()
        context["proxy_man_num"] = len(proxy_man_num)
    except:
        context["software_num"] = 0

    notices = Notice.objects.all().order_by('-time')  #公告
    notices_list = []
    for i in notices[:3]:
        notices_list.append({"admin_name":i.admin_object.username,"time":i.time.strftime("%Y-%m-%d"),"title":i.title,"word":i.word})
    context["notices_list"]=notices_list
    return render(request,"index.html",context)

@login_required
def shop_page(request):
    all_software = Software.objects.all()
    context = {"all_software":all_software}
    return render(request,"page-shop.html",context=context)

@login_required
def shop_detail(request, software_id):
    if request.method == 'GET':
        try:
            user_others_info = Others_info.objects.get(user=request.user)
        except:
            return HttpResponse("出现错误！报告错误号：1000。\n 你可能登陆了多个账户或管理员账户，请登出后再操作！")
        software = Software.objects.get(software_id=software_id)
        context = {"software":software,"money":user_others_info.balance}
        return render(request,'items-detail.html',context=context)

@login_required
def buy_items(request):
    if request.method == 'POST':
        num = request.POST['num']
        sid = request.POST['sid']  #引入
        num = int(num)
        if num<0:
            raise Http404("错了！")
        try:
            software = Software.objects.get(software_id=sid)
        except:
            raise Http404("错了！找不到sid！")
        user = request.user
        try:
            user_others_info = Others_info.objects.get(user=request.user)
        except:
            return HttpResponse("出现错误！报告错误号：1000。\n 你可能登陆了多个账户或管理员账户，请登出后再操作！")
        total_mony = software.software_cost * num
        if user_others_info.balance - total_mony < 0:
            context = {"link":"/shop/item/"+sid+'/',"error_name":"错误","error_name2":"余额不足","error_name3":"您的余额为："+str(user_others_info.balance)}
            return render(request,'page-error.html',context)
        user_others_info.balance = user_others_info.balance - total_mony #扣钱
        user_others_info.save() #保存

        #创建交易
        deal_record = Deal_record.objects.create(deal_code=get_deal_code(),acount=user,money=total_mony,symbol=False,notes=str(software.software_name)+"_数量："+str(num))
        deal_record.save()#保存

        #生成卡。
        for i in range(num):
            code_object = Time_code.objects.create(software=software,time=software.software_each_time,code=get_Code(10),cost=software.software_cost,proxy_man=user,deal_object=deal_record)
            code_object.save()
        return redirect("check_deal",deal_code=deal_record.deal_code)

@login_required
def check_deal(request,deal_code):
        deal_record = Deal_record.objects.get(deal_code=deal_code)
        if deal_record.acount != request.user:
            return redirect("index")
        codes_list = Time_code.objects.filter(deal_object=deal_record)
        context = {"codes_list":codes_list,"deal_record":deal_record}
        return render(request,'table-datatable.html',context=context)


@login_required
def check_all_deal(request):
    all_deal = Deal_record.objects.filter(acount=request.user)
    context = {"all_deal":all_deal}
    return render(request,"page-deal.html",context)


@login_required
def profile_setting(request):
    if request.method == 'GET':
        others_info = Others_info.objects.get(user=request.user)
        context = {"others_info":others_info}
        return render(request,"profile.html",context)
    elif request.method == 'POST':
        opw = request.POST['opw']
        pw = request.POST['pw']
        pwa = request.POST['pwa']
        qq = request.POST['qq']
        ad = request.POST['ad']
        if request.user.email != qq:
            request.user.email = qq
            request.user.save()
            context = {"success": "修改成功！"}
        others_info = Others_info.objects.get(user=request.user)
        if others_info.ad != ad:
            others_info.ad = ad
            others_info.save()
            context = {"success":"修改成功！"}
        try:
            context["others_info"] = others_info
        except:
            context = {"others_info": others_info}
        if opw != '' and pw != '' and pwa != '':
            user = authenticate(username=request.user.username, password=opw)
            if user != None:
                if user.is_active:
                    if pw == pwa:
                        user.set_password(pw)
                        user.save()
                        context['success'] = "修改成功！"
                        return redirect("login")
                    else:
                        context['warn'] = "新密码输入两次错误！请重试"
                        return render(request,'profile.html',context)
                else:
                    context['warn'] = "密码输入错误！请重试！"
                    return render(request,'profile.html',context)
            else:
                context['warn'] = "密码输入错误！请重试！"
                return render(request, 'profile.html', context)
        else:
            return render(request, 'profile.html', context)






