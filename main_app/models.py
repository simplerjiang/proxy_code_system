#数据库模型文件

from django.db import models
from django.contrib.admin.options import BaseModelAdmin
from django.contrib.auth.models import User
import random


"""
这里使用Django自带的User进行储存代理。
User.username 是代理账户名。
User.password 是代理密码，数据库中储存哈希值
User.first_name 
User.last_name 
User.email 都是可选字段，预留给以后的
由于返回值可能是字符串
下面将扩展一个Others_info 模型类，用于存放用户金额，广告，以及TOKEN信息
"""
class Others_info(models.Model):
    user = models.OneToOneField(User)
    balance = models.PositiveIntegerField(verbose_name="用户余额",default=0)
    ad = models.CharField(verbose_name="代理广告",max_length=30)
    TOKEN = models.CharField(verbose_name="API密链",max_length=15,unique=True)




def get_TOKEN(num=15): #获取随机TOKEN，通过传入位数。
    while 1:
        a = "1234567890"
        b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sa = []
        for i in range(num//2):
            sa.append(random.choice(b))
            sa.append(random.choice(a))
        sa = "".join(sa)
        try:
            Others_info.objects.get(TOKEN=sa)
        except Others_info.DoesNotExist:
            return sa
"""
#暂时不需要
class web_admin(models.Model):
    admin_name = models.CharField(verbose_name="管理员账户名", max_length=30)
    admin_password = models.CharField(verbose_name="管理员密码", max_length=30)
"""
class Admin_code(models.Model):
    code = models.CharField(verbose_name="API用密链",max_length=50,default=get_TOKEN(15))

class Software(models.Model):
    software_id = models.PositiveIntegerField(verbose_name="软件ID", unique=True)
    software_name = models.CharField(verbose_name="软件名", max_length=30)
    software_version_number = models.CharField(verbose_name="软件版本号", max_length=30)

    def __str__(self):
        return self.software_name

    def return_id(self):
        return self.software_id


class Authorization(models.Model):
    software = models.ForeignKey(Software, verbose_name="软件对象")
    customer_QQ = models.PositiveIntegerField(verbose_name="客户的QQ")
    proxy_man = models.ForeignKey(User,verbose_name="代理")
    bot_QQ = models.PositiveIntegerField("机器人的QQ")
    begin_time = models.DateField(verbose_name="创建时间",auto_now_add=True)
    deadline_time = models.DateField(verbose_name="到期时间",auto_now_add=True)


class Time_code(models.Model):
    software = models.ForeignKey(Software, verbose_name="软件对象")
    time = models.PositiveIntegerField(verbose_name="时长")
    code = models.CharField(verbose_name="卡密",max_length=10)
    cost = models.PositiveIntegerField(verbose_name="价格")
    proxy_man = models.ForeignKey(User,verbose_name="代理",null=True)
    used = models.BooleanField(verbose_name="是否使用过",default=False)



