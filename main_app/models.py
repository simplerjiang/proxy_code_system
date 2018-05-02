#数据库模型文件

from django.db import models
from django.contrib.admin.options import BaseModelAdmin
from django.contrib.auth.models import User
import random


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
            User.objects.get(email=sa)
        except:
            return sa

"""
这里使用Django自带的User进行储存代理。
User.username 是代理账户名。
User.password 是代理密码，数据库中储存哈希值
User.first_name 是代理广告
User.last_name 是账户金额
User.email 是随机生成的TOKEN，每次登陆会有修改。
由于返回值可能是字符串，所以要进行转换类型
"""

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

