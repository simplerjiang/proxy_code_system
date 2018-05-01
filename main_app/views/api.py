from django.shortcuts import render
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse #用来进行命名空间的反调用
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse,HttpResponseRedirect #HttpResponseRedirect是用于进行url进行跳转
from main_app.models import *
from django.contrib.auth.models import User
import json

def dump_and_response(data):
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
def admin_code_check(admin_code):
    try:
        Admin_code.objects.get(code = admin_code)
        return True
    except:
        return False

"""
代理账户管理API
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

def admin_proxy_account_add_API(request):
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

def admin_proxy_account_topup(request):
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

def admin_proxy_account_balance_setup(request):
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
def proxy_account_balance_check(request):
    if request.method == "POST":
        return dump_and_response("Error, bad request method POST")
    proxy_username = request.GET['proxy_username']
    try:
        user_object = User.objects.get_by_natural_key(username=proxy_username)
        return dump_and_response(user_object.last_name)
    except User.DoesNotExist:
        return dump_and_response("Proxy account not existed")

