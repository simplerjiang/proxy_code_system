#coding=utf-8
"""
警告！在请求中请勿以username 及password作为http请求的参数名！
"""
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse #用来进行命名空间的反调用
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse,HttpResponseRedirect #HttpResponseRedirect是用于进行url进行跳转
from main_app.models import *
from django.contrib.auth.models import User
import json

def dump_and_response(data): #checked
    return HttpResponse(json.dumps(data), content_type="application/json")


def api_test(request):
    try:
        test = Admin_code.objects.get(code = request.GET["admin_code"])
        return dump_and_response(test.code)
    except Admin_code.DoesNotExist:
        return dump_and_response(["error","reson"])
"""
以下是管理员API
"""
def admin_code_check(admin_code): #checked
    try:
        Admin_code.objects.get(code = admin_code)
        return True
    except:
        return False

"""
代理账户开户API
url:http://127.0.0.1:8000/api/admin_proxy_account_add_api/?admin_code=testtest&proxy_username=Kong1&proxy_password=testtest
参数:
admin_code = 管理员代码
proxy_username = 代理账户名
proxy_password = 代理密码
proxy_ad = 代理广告（不写就是为空字符串)
proxy_balance = 代理账户金额（不写默认为0)
返回值： (全部json格式）
"Fail,account already existed" 账户已存在，创建失败
"Success" 创建成功
"Error, admin code wrong"  管理员代码错误
"Error,bad request method POST" 错误的请求模式
"""

def admin_proxy_account_add_API(request): #已测试
    if request.method == "POST":
        return dump_and_response("Error,bad request method POST")
    admin_code = request.GET['admin_code']
    if not admin_code_check(admin_code):
        return dump_and_response("Error, admin code wrong")
    proxy_username = request.GET['proxy_username']
    proxy_password = request.GET['proxy_password']
    try:
        proxy_ad = request.GET['proxy_ad']
    except:
        proxy_ad = ''
    try:
        proxy_balance = request.GET['proxy_balance']
    except:
        proxy_balance = 0
    user_object = authenticate(username = proxy_username,password = proxy_password)
    if user_object is None:
        user_object = User.objects.create_user(username=proxy_username,password=proxy_password,first_name=proxy_ad,last_name=proxy_balance)
        user_object.save()
        return dump_and_response("Success")
    else:
        return dump_and_response("Fail,account already existed")


"""
代理账户充值
url:url:http://127.0.0.1:8000/api/admin_proxy_account_topup/?admin_code=testtest&proxy_username=Kong2&money=30

参数：
admin_code 管理员代码
proxy_username 代理账号
money 添加金额

返回值:
["Success", "90"] 成功，第二个参数是目前的金额
"Error, admin code wrong"  管理员代码错误
"Error,bad request method POST" 错误的请求模式
"Proxy account not existed" 代理账号不存在
"""

def admin_proxy_account_topup(request): #已测试
    if request.method == "POST":
        return dump_and_response("Error,bad request method POST")
    admin_code = request.GET['admin_code']
    if not admin_code_check(admin_code):
        return dump_and_response("Error, admin code wrong")
    proxy_username = request.GET['proxy_username']
    money = request.GET['money']
    try:
        user_object = User.objects.get_by_natural_key(username=proxy_username)
        user_balance = user_object.last_name
        user_balance = str(int(user_balance) +int(money))
        user_object.last_name = user_balance
        user_object.save()
        return dump_and_response(["Success",user_object.last_name])
    except User.DoesNotExist:
        return dump_and_response("Proxy account not existed")

"""
代理账户金额修改
注意！此API功能用于清零，如果操作不当可能造成严重后果。且输入值必须大于等于0

url:http://127.0.0.1:8000/api/admin_proxy_account_balance_setup/?admin_code=testtest&proxy_username=Kong2&money=30

参数：
admin_code 管理员代码
proxy_username 代理账号
money 设置金钱

返回值:
["Success", "90"] 成功，第二个参数是目前的金额
"Error, admin code wrong"  管理员代码错误
"Error,bad request method POST" 错误的请求模式
"Proxy account not existed" 代理账号不存在
"Error, money type wrong" money参数不是一个数字
"Error, money less than 0" money参数小于0
"""

def admin_proxy_account_balance_setup(request): #已测试
    if request.method == "POST":
        return dump_and_response("Error, bad request method POST")
    admin_code = request.GET['admin_code']
    if not admin_code_check(admin_code):
        return dump_and_response("Error, admin code wrong")
    proxy_username = request.GET['proxy_username']
    money = request.GET['money']
    try:
        money = int(money)
    except ValueError:
        return dump_and_response("Error, money type wrong")
    if money < 0:
        return dump_and_response("Error, money less than 0")
    try:
        user_object = User.objects.get_by_natural_key(username=proxy_username)
        user_object.last_name = str(money)
        user_object.save()
        return dump_and_response(["Success",user_object.last_name])
    except User.DoesNotExist:
        return dump_and_response("Proxy account not existed")

"""
代理金额查询 (管理员及代理可用，不需要管理员代码）
url:

参数：
proxy_username 代理账号
返回值：
"30" 正确返回则返回目前余额
"Error,bad request method POST" 错误的请求模式
"Proxy account not existed" 代理账号不存在
"""
def proxy_account_balance_check(request): #已测试
    if request.method == "POST":
        return dump_and_response("Error, bad request method POST")
    proxy_username = request.GET['proxy_username']
    try:
        user_object = User.objects.get_by_natural_key(username=proxy_username)
        return dump_and_response(user_object.last_name)
    except User.DoesNotExist:
        return dump_and_response("Proxy account not existed")

"""
管理员用——修改代理账号密码
url:http://127.0.0.1:8000/api/admin_proxy_account_change_password/?proxy_username=Kong&admin_code=tedttest&proxy_new_password=MyNewPassword
参数：
admin_code 管理员代码
proxy_username 代理账号
proxy_new_password 新密码
返回值：
"success" 代表修改成功
"Error,admin code wrong!" 管理员密链错误
"Error, account is Not exsited" 如果账户不存在则返回此警告
"Error,bad request method POST" 错误的请求模式
"""

def admin_proxy_account_change_password(request): #测试
    if request.method is "POST":
        return dump_and_response("Error, bad request method POST")
    admin_code = request.GET["admin_code"]
    if not admin_code_check(admin_code):
        return dump_and_response("Error,admin code wrong!")
    username = request.GET["proxy_username"]
    new_password = request.GET["proxy_new_password"]
    try:
        user = User.objects.get(username=username)
        user.set_password(new_password)
        user.save()
        return dump_and_response("success")
    except User.DoesNotExist:
        return dump_and_response("Error, account is Not exsited")



"""
以下为代理可用API
"""

"""
代理登陆
代理登陆后会返回一个TOKEN(密链）,代理的其他操作API都需要此密链，
每次调用一次登陆函数就会重新定义并返回一次密链，所以具有时效性
url:http://127.0.0.1:8000/api/proxy_account_login/?proxy_username=d&proxy_password=XXXXX

参数：
proxy_username 用户名
proxy_password 密码

返回值：
XXXXXXXXXXXX 如果成功，将返回15位数的特定密链（这里被称为TOKEN)
"Error, account is Not exsited or password is fail" 如果账号密码或账户不存在都返回此警告
"Error,bad request method POST" 错误的请求模式

"""

def proxy_account_login(request): #已测试
    if request.method is "POST":
        return dump_and_response("Error, bad request method POST")
    username = request.GET["proxy_username"]
    password = request.GET["proxy_password"]
    user = authenticate(username=username,password=password)
    if user != None:
        if user.is_active:
            user.email = get_TOKEN(15)
            user.save()
            return dump_and_response(user.email)
        else:
            return dump_and_response("Error, account is Not exsited or password is fail")
    else:
        return dump_and_response("Error, account is Not exsited or password is fail")


"""
代理修改代理账户密码
参数：
proxy_username 用户名
proxy_password 密码
proxy_new_password 新的密码

返回值：
"success" 代表修改成功
"Error, account is Not exsited or password is fail" 如果账号密码或账户不存在都返回此警告
"Error,bad request method POST" 错误的请求模式
"""

def proxy_account_change_password(request): #已测试
    if request.method is "POST":
        return dump_and_response("Error, bad request method POST")
    username = request.GET["proxy_username"]
    password = request.GET["proxy_password"]
    user = authenticate(username=username,password=password)
    if user != None:
        if user.is_active:
            new_password = request.GET["proxy_new_password"]
            user.set_password(new_password)
            user.save()
            return dump_and_response("success")
        else:
            return dump_and_response("Error, account is Not exsited or password is fail")
    else:
        return dump_and_response("Error, account is Not exsited or password is fail")


"""
代理设置广告

参数：
token 代理客户login函数成功后返回的密链，每个账号都有一个独立的密链，并且每次登陆后都会返回一个新的密链
ad 需要设置的广告（15字以内）
返回值：
"success" 修改成功
"Error, account is Not exsited or token is fail" 如果token错误或账户不存在都返回此警告
"Error,bad request method POST" 错误的请求模式
"""
def proxy_account_ad_change(request): #已测试
    if request.method is "POST":
        return dump_and_response("Error, bad request method POST")
    token = request.GET['token']
    ad = request.GET['ad']
    try:
        user = User.objects.get(email = token)
    except:
        return dump_and_response("Error, account is Not exsited or token is fail")
    user.first_name = ad
    user.save()
    return dump_and_response("success")

