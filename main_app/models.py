#数据库模型文件

from django.db import models
from django.contrib.admin.options import BaseModelAdmin
from django.contrib.auth.models import User
import random

"""
这里使用Django自带的User进行储存代理。
User.username 是代理账户名。
User.password 是代理密码，数据库中储存哈希值
User.first_name 是代理广告
User.last_name 是账户金额
User.email 可选
由于返回值可能是字符串，所以要进行转换类型
"""

"""
#暂时不需要
class web_admin(models.Model):
    admin_name = models.CharField(verbose_name="管理员账户名", max_length=30)
    admin_password = models.CharField(verbose_name="管理员密码", max_length=30)
"""


class software(models.Model):
    software_id = models.PositiveIntegerField(verbose_name="软件ID", unique=True)
    software_name = models.CharField(verbose_name="软件名", max_length=30)
    software_version_number = models.CharField(verbose_name="软件版本号", max_length=30)

    def __str__(self):
        return self.software_name

    def return_id(self):
        return self.software_id


class authorization(models.Model):
    software = models.ForeignKey(software, verbose_name="软件对象")
    customer_QQ = models.PositiveIntegerField(verbose_name="客户的QQ")
    proxy_man = models.ForeignKey(User,verbose_name="代理")
    bot_QQ = models.PositiveIntegerField("机器人的QQ")
    begin_time = models.DateField(verbose_name="创建时间",auto_now_add=True)
    deadline_time = models.DateField(verbose_name="到期时间",auto_now_add=True)


class time_code(models.Model):
    software = models.ForeignKey(software, verbose_name="软件对象")
    time = models.PositiveIntegerField(verbose_name="时长")
    code = models.CharField(verbose_name="卡密",max_length=10)
    cost = models.PositiveIntegerField(verbose_name="价格")
