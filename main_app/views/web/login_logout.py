from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse #用来进行命名空间的反调用
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse,HttpResponseRedirect,Http404 #HttpResponseRedirect是用于进行url进行跳转
from main_app.models import *
from datetime import date,timedelta
from .time_deal import *
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == "POST":
        username = request.POST['un']
        password = request.POST['pw']
        user = authenticate(username=username, password=password)

        if user != None:
            if user.is_active:
                login(request, user)
                try:
                    next_page = request.POST['next']
                    return redirect(next_page)
                except:
                    return redirect("index")
            else:
                context = {"warn":"用户不存在或错误"}
                return render(request,'page-login.html',context=context)
        else:
            context = {"warn": "用户不存在或错误"}
            return render(request, 'page-login.html', context=context)
    else:
        try:
            context = {"next":request.GET['next']}
            return render(request,'page-login.html',context)
        except:
            return render(request,'page-login.html')

def reg(request):
    if request.method == "POST":
        username = request.POST['un']
        password = request.POST['pw']
        passwordagain = request.POST['pwa']
        qq = request.POST['qq']
        try:
            qq = int(qq)
            qq = str(qq)
        except:
            return render(request, 'page-register.html', context={"warn": "请输入正确QQ号！"})
        if password != passwordagain:
            return render(request,'page-register.html',context={"warn":"密码两次输入错误！"})
        try:
            User.objects.get(username=username)
            return render(request,"page-register.html",context={"warn":"用户名已存在！"})
        except User.DoesNotExist:
            user = User.objects.create_user(username=username,email=qq,password=password)
            others_info = Others_info.objects.create(user=user,TOKEN=get_TOKEN())
            others_info.save()
        user = authenticate(username=username,password=password)
        login(request,user)
        try:
            next_page = request.POST['next']
            return redirect(next_page)
        except:
            return redirect("index")
    else:
        if request.user.is_anonymous():
            try:
                context = {"next": request.GET['next']}
                return render(request, 'page-register.html', context)
            except:
                return render(request, 'page-register.html')
        else:
            return redirect("index")
        

@login_required
def log_out_view(request): #logout
    logout(request)
    return render(request,'page-login.html',context={"warn":"登出成功"})