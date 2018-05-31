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



"""
可通过TOKEN或username找代理账号
返回一个列表，第一个是User对象，第二个是Others_info对象。
"""
def get_proxy_account(TOKEN=None,username=None,pk_id = None):
    if TOKEN != None:
        try:
            user_others_info = Others_info.objects.get(TOKEN=TOKEN)
            return [user_others_info.user,user_others_info]
        except:
            return False
    elif username != None:
        try:
            user_object = User.objects.get_by_natural_key(username=username)
            user_others_info = Others_info.objects.get(user=user_object)
            return [user_object,user_others_info]
        except:
            return False
    elif pk_id != None:
        try:
            user_object = User.objects.get(pk=pk_id)
            user_others_info = Others_info.objects.get(user=user_object)
            return  [user_object,user_others_info]
        except:
            return False

def get_my_up_proxy(user): #传入一个get_proxy_account函数的返回列表，user[0]是user对象，user[1]是others_info 对象
    if user[1].up_proxy != 0: #如果传入的账号有上级代理
        a = []
        up_user = get_proxy_account(pk_id=user[1].up_proxy) #获取他上级代理的特殊对象
        a.append(up_user) #添加到列表a中
        b = get_my_up_proxy(up_user) #递归获取它的上级
        if b != False: #如果它的存在，添加到列表中，并返回。
            c = a+b
            return c
        else: #返回a
            return a

    else: #如果传入的账号没有上级代理，返回False
        return False


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

    context['discount'] = "%.1f" % (10 - user_other_info.level *0.5)
    context["my_level"] = user_other_info.level

    notices = Notice.objects.all().order_by('-time')  #公告
    notices_list = []
    for i in notices[:3]:
        notices_list.append({"admin_name":i.admin_object.username,"time":i.time.strftime("%Y-%m-%d"),"title":i.title,"word":i.word})
    context["notices_list"]=notices_list
    return render(request,"index.html",context)

@login_required
def shop_page(request):
    all_software = Software.objects.all()
    all_software_list = []
    others_info_object = Others_info.objects.get(user=request.user)
    discount = Decimal(1 - (others_info_object.level * 0.05))  # 折扣，输出一个浮点数
    for i in all_software:
        a = {
            "software_cost":"%.2f" % (i.software_cost*discount),
            "software_id":i.software_id,
            "software_name":i.software_name,
            "software_each_time":i.software_each_time,
            "software_version_number":i.software_version_number,
             }
        all_software_list.append(a)

    context = {"all_software":all_software_list}
    return render(request,"page-shop.html",context=context)

@login_required
def shop_detail(request, software_id):
    if request.method == 'GET':
        try:
            user_others_info = Others_info.objects.get(user=request.user)
        except:
            return HttpResponse("出现错误！报告错误号：1000。\n 你可能登陆了多个账户或管理员账户，请登出后再操作！")
        discount = Decimal(1 - (user_others_info.level * 0.05))  # 折扣，输出一个浮点数
        software = Software.objects.get(software_id=software_id)
        software_list = {
            "software_cost":"%.2f" % (software.software_cost*discount),
            "software_id":software.software_id,
            "software_name":software.software_name,
            "software_each_time":software.software_each_time,
            "software_version_number":software.software_version_number,
        }
        context = {"software": software_list, "money": user_others_info.balance}
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
        user = get_proxy_account(username=user.username)
        if user == False:
            return HttpResponse("出现错误！报告错误号：1000。\n 你可能登陆了多个账户或管理员账户，请登出后再操作！")
        #生成本账号折扣
        discount = Decimal(1 - (user[1].level * 0.05))

        cost = software.software_cost * num * discount  # 生成此次提卡价格
        count = user[1].balance - (cost)  # 减了以后得余额
        if count < 0: #余额错误，返回错误页面
            context = {"link":"/shop/item/"+sid+'/',"error_name":"错误","error_name2":"余额不足","error_name3":"您的余额为："+str(user[1].balance)}
            return render(request,'page-error.html',context)
        user[1].balance -= cost #扣钱
        user[1].save() #保存

        #创建交易
        deal_record = Deal_record.objects.create(deal_code=get_deal_code(),acount=user[0],money=cost,symbol=False,notes="提卡-"+str(software.software_name)+"_数量："+str(num))
        deal_record.save()#保存

        all_up_proxy = get_my_up_proxy(user)  # 获取所有上级代理的账号对象
        # 结算出最顶级上级的价格，减去本用户的价格，获取需要分配的金额
        if all_up_proxy != False:
            highest_proxy = all_up_proxy[-1]
            dirty_money = cost - (software.software_cost * num * Decimal(1 - (highest_proxy[1].level * 0.05)))  # 生成中间差价

            # 进入多层代理账号循环
            for i in range(len(all_up_proxy)):
                if i == 0:  # 如果匹配到是第0个号，就是本账号的直属上级代理。将他与本账号的cost价格相减，得出它的利润
                    cost_up = software.software_cost * num * Decimal(
                        1 - (all_up_proxy[i][1].level * 0.05))  # 生成本次循环账号的代理价格
                    sub_money = cost - cost_up  # 获得这层代理的中间差价
                    # 生成订单
                    up_deal_record = Deal_record.objects.create(deal_code=get_deal_code(5), acount=all_up_proxy[i][0],
                                                                money=sub_money, symbol=True,
                                                                notes="下级代理提卡的提成：" + "%.2f" % sub_money)
                    up_deal_record.save()
                    # 完成加钱
                    all_up_proxy[i][1].balance += sub_money
                    all_up_proxy[i][1].save()
                else:
                    sub_money = cost_up - (software.software_cost * num * Decimal(
                        1 - (all_up_proxy[i][1].level * 0.05)))  # 获得这层代理的中间差价
                    cost_up = software.software_cost * num * Decimal(
                        1 - (all_up_proxy[i][1].level * 0.05))  # 生成本次循环账号的代理价格，以供下次循环使用。
                    # 生成订单
                    up_deal_record = Deal_record.objects.create(deal_code=get_deal_code(5), acount=all_up_proxy[i][0],
                                                                money=sub_money, symbol=True,
                                                                notes="下级代理提卡的提成：" + "%.2f" % sub_money)
                    up_deal_record.save()
                    # 完成加钱
                    all_up_proxy[i][1].balance += sub_money
                    all_up_proxy[i][1].save()

        #生成卡。
        for i in range(num):
            code_object = Time_code.objects.create(software=software,time=software.software_each_time,code=get_Code(10),cost=software.software_cost*discount,proxy_man=user[0],deal_object=deal_record)
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
    all_deal = Deal_record.objects.filter(acount=request.user).order_by("time")
    all_deal = all_deal.reverse()
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
        if opw != '' or pw != '' or pwa != '':
            user = authenticate(username=request.user.username, password=opw)
            if user != None:
                if user.is_active:
                    if pw == pwa:
                        if pw == '' or pwa == '':
                            context['warn'] = "请输入新密码！"
                            return render(request, 'profile.html', context)
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


@login_required
def check_all_auth(request):
    context = {}
    try:  #查找授权
        auths = Authorization.objects.filter(proxy_man=request.user).order_by('id')
        auths_list =[]
        auths = auths.reverse()
        for i in auths:
            a = {"software":i.software,"customer_QQ":i.customer_QQ,"bot_QQ":i.bot_QQ,"begin_time":i.begin_time,"deadline_time":i.deadline_time,"pk":i.pk}
            auths_list.append(a)
            if i.deadline_time < timezone.now():
                a["auths_state"] = False
            else:
                a["auths_state"] = True
        context["auths_list"] = auths_list
    except:
        pass

    return render(request,'page-auth.html',context)

@login_required
def check_auth(request,pk):
    if request.method == "GET":
        context = {"pk":pk}
        try:
            auth = Authorization.objects.get(pk=pk)
            if auth.proxy_man != request.user:
                return Http404("此授权不属于此账户！")
            context["auth"] = auth
            return render(request,'auth-detail.html',context=context)
        except Authorization.DoesNotExist:
            raise Http404("未找到！错误！")
    elif request.method == "POST":
        context ={"pk":pk}
        try:
            auth = Authorization.objects.get(pk=pk)
            if auth.proxy_man != request.user:
                raise Http404("此授权不属于此账户！")
            elif str(auth.bot_QQ) != request.POST['qq']:
                auth.bot_QQ = request.POST['qq']
                auth.save()
                context['success'] = "机器人QQ修改成功！"

        except Authorization.DoesNotExist:
            raise Http404("找不到！错误！")
        context['auth'] = auth
        return render(request, 'auth-detail.html', context=context)


@login_required
def check_all_down_proxy(request): #查看所有下级代理
    user_id = request.user.id
    all_proxy_list = Others_info.objects.filter(up_proxy=user_id)
    context = {"all_proxy_list":all_proxy_list}
    return render(request,'proxy_list.html',context=context)

@login_required
def change_down_proxy_info(request,pk):
    if request.method == 'GET':
        user_id = request.user.id
        try:
            down_user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404("干你")

        #检查是否是下级代理。
        down_user = get_proxy_account(username=down_user.username)
        if down_user[1].up_proxy != int(user_id):
            raise Http404("想干啥？")
        else:
            context = {"down_user_object":down_user[0],"down_user_others":down_user[1]}
            return render(request,'down_proxy_detail.html',context)
    elif request.method == "POST":
        user_id = request.user.id
        user = get_proxy_account(pk_id=user_id)
        try:
            down_user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404("干你")
        # 检查是否是下级代理。
        down_user = get_proxy_account(username=down_user.username)
        if down_user[1].up_proxy != int(user_id):
            raise Http404("想干啥？")
        context = {"down_user_object": down_user[0], "down_user_others": down_user[1]}
        level = request.POST['level']
        qq = request.POST['qq']
        if level == '' or qq == '':
            context['warn'] = "修改失败！不可以清除信息！"
            return render(request, 'down_proxy_detail.html', context)

        try:
            level = int(level)
        except:
            context['warn'] = "请输入正确的等级！（例如：1）"
            return render(request,'down_proxy_detail.html',context)

        if level <= 0:
            context['warn'] = "请输入大于0的等级！（例如：1）"
            return render(request, 'down_proxy_detail.html', context)

        if level >= user[1].level:
            context['warn'] = "请输入小于的自身！（例如：1）"
            return render(request, 'down_proxy_detail.html', context)

        if level != down_user[1].level:
            down_user[1].level = level
            down_user[1].save()
            context["success"] = "等级修改成功！"

        if qq != down_user[0].email:
            down_user[0].email = qq
            down_user[0].save()
            context['success'] = 'QQ号修改成功！'

        if "pw" in request.POST and "pwa" in request.POST:
            pw = request.POST['pw']
            pwa = request.POST['pwa']
            if pw != '' and pwa != '':
                if pw == pwa:
                    down_user[0].set_password(pw)
                    down_user[0].save()

                    context['success'] = "密码修改成功！"
                    return render(request,"down_proxy_detail.html",context)
                else:
                    context['warn'] = "新密码输入两次错误！请重试"
                    return render(request, 'down_proxy_detail.html', context)
            else:
                if pw != '' or pwa != '':
                    context['warn'] = "请输入新密码!"
                    return render(request, 'down_proxy_detail.html', context)
                else:
                    return render(request, 'down_proxy_detail.html', context)
        else:
            return render(request,'down_proxy_detail.html',context)


@login_required
def create_new_down_account(request):
    if request.method == "GET":
        user = get_proxy_account(username=request.user.username)
        level = str(user[1].level - 1)
        context = {"level":level}
        return render(request,"add_down_proxy.html",context)
    elif request.method == "POST":
        user = get_proxy_account(username=request.user.username)
        context = {"level":str(user[1].level - 1)}
        if "proxy_username" in request.POST:
            proxy_username = request.POST['proxy_username']
            try:
                User.objects.get_by_natural_key(username=proxy_username)
                context['warn'] = "用户名已存在，请重试！"
                return render(request, 'add_down_proxy.html', context)
            except User.DoesNotExist:
                pass

        else:
            return render(request, 'add_down_proxy.html', context)

        if "pw" in request.POST and "pwa" in request.POST:
            pw = request.POST['pw']
            pwa = request.POST['pwa']
            if pw != pwa:
                context['warn'] = "密码二次验证输入错误！请重试"
                return render(request, 'add_down_proxy.html', context)
            elif pw == '' or pwa == '':
                context['warn'] = "请输入密码！请重试"
                return render(request, 'add_down_proxy.html', context)
        else:#错误提示
            context['warn'] = "请输入密码！请重试"
            return render(request, 'add_down_proxy.html', context)
        if "qq" in request.POST:
            qq = request.POST['qq']
            if qq == '':
                context['warn'] = "请输入QQ号！请重试"
                return render(request, 'add_down_proxy.html', context)
        else:
            context['warn'] = "请输入QQ号！请重试"
            return render(request, 'add_down_proxy.html', context)
        if "level" in request.POST:
            down_level = request.POST['level']
            try:
                down_level = int(down_level)
            except:
                context['warn'] = "请输入正确的等级！（例如：1）"
                return render(request, 'add_down_proxy.html', context)
            if down_level <= 0:
                context['warn'] = "请输入正确的等级！（例如：1）"
                return render(request, 'add_down_proxy.html', context)
            elif down_level >= user[1].level:
                context['warn'] = "请输入小于自身账户的等级！"
                return render(request, 'add_down_proxy.html', context)
        else:
            context['warn'] = "请输入新账号的等级！请重试"
            return render(request, 'add_down_proxy.html', context)
        down_user = User.objects.create(username=proxy_username,password=pw,email=qq)
        down_user.save()
        down_user_others = Others_info.objects.create(user=down_user,TOKEN=get_TOKEN(),level=down_level,up_proxy=user[0].id)
        down_user_others.save()
        return redirect("change_down_proxy_info",down_user.id)

@login_required
def get_money(request):
    if request.method == "GET":
        user = get_proxy_account(username=request.user.username)
        context = {"balance":user[1].balance}
        return render(request,"getmoney.html",context)

    elif request.method == "POST":
        user = get_proxy_account(username=request.user.username)
        context = {"balance":user[1].balance}
        money = request.POST['money']
        money_account_kind = request.POST['money_account_kind']
        money_account_num = request.POST['money_account_num']
        money_account_name = request.POST['money_account_name']
        if money == '' or money_account_num == '' or money_account_name == '' or money_account_kind == '':
            context["warn"] = "请输入完整信息！"
            return render(request,"getmoney.html",context)

        try:
            money = Decimal(money)
        except decimal.InvalidOperation:
            context["warn"] = "请输入正确的提款金额"
            return render(request,"getmoney.html",context)

        if user[1].balance - money < 0:
            context['warn'] = "账户余额不足！请重试！"
            return render(request,"getmoney.html",context)

        #开始扣费
        user[1].balance -= money
        user[1].save()
        #创建订单
        deal_record = Deal_record.objects.create(deal_code=get_deal_code(5),acount=user[0],money=money,symbol=False,notes="网页提现操作")
        deal_record.save()

        #创建提现单
        get_money_object = Getmoney.objects.create(proxy_account=user[0],money=money,money_account_name=money_account_kind,money_account_num=money_account_num,account_name=money_account_name)
        get_money_object.save()
        return redirect("check_all_deal")


@login_required
def transfer(request):
    if request.method == "GET":
        user = get_proxy_account(username=request.user.username)
        down_account_list = Others_info.objects.filter(up_proxy=user[0].id)
        context = {"down_account_list":down_account_list,"balance":user[1].balance}
        return render(request,"transfer.html",context)

    elif request.method == "POST":
        user=get_proxy_account(username=request.user.username)
        down_account_list = Others_info.objects.filter(up_proxy=user[0].id)
        context = {"down_account_list":down_account_list,"balance":user[1].balance}

        money = request.POST['money']
        account = request.POST['account']
        if money == '' or account == '':
            context['warn'] = "请输入转账信息！"
            return render(request,"transfer.html",context)

        if account == '0':
            return render(request,'transfer.html',context)

        try:
            money = Decimal(money)
        except:
            context['warn'] = "请输入正确的金额"
            return render(request, 'transfer.html', context)
        if money <= 0:
            context['warn'] = "请输入正确的金额"
            return render(request, 'transfer.html', context)

        if user[1].balance - money < 0:
            context['warn'] = "你的余额不足，请重新尝试！"
            return render(request, 'transfer.html', context)

        account = int(account)
        target_account = get_proxy_account(pk_id=account)
        if target_account == False:
            context['warn'] = "账号错误！请重新尝试！"
            return render(request, 'transfer.html', context)
        if target_account[1].up_proxy != user[0].id:
            context['warn'] = "账号不属于你的下级代理！请重试！"
            return render(request, 'transfer.html', context)
        #开始扣款
        user[1].balance -= money
        user[1].save()

        #转出者创建订单
        my_deal_record = Deal_record.objects.create(deal_code=get_deal_code(5),acount=user[0],money=money,symbol=False,notes="网页转账-转出")
        my_deal_record.save()

        #转入者收款
        target_account[1].balance += money #收款
        target_account[1].save()

        target_deal_record = Deal_record.objects.create(deal_code=get_deal_code(5),acount=target_account[0],money=money,notes="网页转账-转入")
        target_deal_record.save()

        context['success'] = "成功转账！收款账号：" + target_account[0].username + "  金额：%.2f" % money
        context['balance'] = user[1].balance
        return render(request,'transfer.html',context)



