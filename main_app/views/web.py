from django.shortcuts import render
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse #用来进行命名空间的反调用
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse,HttpResponseRedirect #HttpResponseRedirect是用于进行url进行跳转
from main_app.models import *
from datetime import date,timedelta
from .time_deal import *

def api_test(request):
    auth_objects = Authorization.objects.get(customer_QQ="1231231")
    time_objects = auth_objects.deadline_time
    auth_objects.deadline_time = time_objects
    time_objects = auth_objects.deadline_time
    local_time = convert_timezone(time_objects)
    auth_objects.save()
    return HttpResponse(local_time.strftime("%Y-%m-%d %H:%M:%S"))


