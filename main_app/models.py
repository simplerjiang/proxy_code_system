#数据库模型文件

from django.db import models
from django.contrib.admin.options import BaseModelAdmin
from django.contrib.auth.models import User
import random
import datetime
import django.utils.timezone  as timezone

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

def get1_Code(num=15): #获取随机TOKEN，通过传入位数。
    while 1:
        a = "1234567890"
        b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sa = []
        for i in range(num//2):
            sa.append(random.choice(b))
            sa.append(random.choice(a))
        sa = "".join(sa)
        return sa


class Others_info(models.Model):
    user = models.OneToOneField(User)
    balance = models.DecimalField(max_digits=8,decimal_places=2,verbose_name="用户余额",default=0)
    ad = models.CharField(verbose_name="代理广告",max_length=30,default="")
    TOKEN = models.CharField(verbose_name="API密链",max_length=15,unique=True)
    level = models.PositiveIntegerField(verbose_name="等级",default=1)
    up_proxy = models.PositiveIntegerField(verbose_name="上级（默认为0，代表没有上级）",default=0)

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
    code = models.CharField(verbose_name="API用密链",max_length=50)

    def __str__(self):
        return self.code+"(此为管理员API密链）"

class Software(models.Model):
    software_id = models.PositiveIntegerField(verbose_name="软件ID", unique=True)
    software_name = models.CharField(verbose_name="软件名", max_length=30)
    software_version_number = models.CharField(verbose_name="软件版本号", max_length=30,default="V1.0")
    software_each_time = models.PositiveIntegerField(verbose_name="套餐时间（按小时计算）",default=720)
    software_cost = models.DecimalField(max_digits=8,decimal_places=2,verbose_name="软件价格",default=0)
    software_try = models.BooleanField(verbose_name="是否开启试用",default=False)
    software_try_hours = models.PositiveIntegerField(verbose_name="试用时长",default=0)
    def __str__(self):
        return self.software_name+"  软件ID:"+str(self.software_id)

class Getmoney(models.Model):
    time = models.DateTimeField(verbose_name="申请时间",auto_now_add=True)
    proxy_account = models.ForeignKey(User,verbose_name="代理账号对象")
    money = models.PositiveIntegerField(verbose_name="提现金额",default=0)
    money_account_name = models.CharField(verbose_name="提现账号种类",max_length=100)#微信,支付宝，QQ
    money_account_num = models.CharField(verbose_name="提现账号",max_length=100)
    account_name  = models.CharField(verbose_name="户主名",max_length=100,blank=True)
    flag = models.BooleanField(verbose_name="是否完成提现",default=False)
    finished_time = models.DateTimeField(verbose_name="完成时间",auto_now=True)
    def __str__(self):
        if self.flag == False:
            return "未完成！    用户：" + self.proxy_account.username + "   金额：" + "%.2f" % self.money + "   方式：" + self.money_account_name + "  提现账户：" + self.money_account_num + "    户主名：" + self.account_name
        else:
            return "已完成！    用户：" + self.proxy_account.username + "   金额：" + "%.2f" % self.money + "   方式：" + self.money_account_name + "  提现账户：" + self.money_account_num + "    户主名：" + self.account_name
class Deal_record(models.Model):
    time = models.DateTimeField(verbose_name="交易时间",auto_now_add=True)
    deal_code = models.CharField(verbose_name="交易编号",max_length=5)
    acount = models.ForeignKey(User,verbose_name="交易账户")
    money = models.DecimalField(max_digits=8,decimal_places=2,verbose_name="交易金额",default=0)
    symbol =models.BooleanField(default=True,verbose_name="正负符号") #如果为True，就是交易为入账，如果为负，账户出账
    notes = models.CharField(default="无",verbose_name="交易备注",max_length=30,blank=True)


class Authorization(models.Model):
    software = models.ForeignKey(Software, verbose_name="软件对象")
    customer_QQ = models.PositiveIntegerField(verbose_name="客户的QQ")
    proxy_man = models.ForeignKey(User,verbose_name="代理",blank=True,null=True)
    bot_QQ = models.PositiveIntegerField("机器人的QQ")
    begin_time = models.DateField(verbose_name="创建时间",auto_now_add=True)
    deadline_time = models.DateTimeField(verbose_name="到期时间",default=timezone.now)



class Time_code(models.Model):
    software = models.ForeignKey(Software, verbose_name="软件对象")
    time = models.PositiveIntegerField(verbose_name="时长")
    code = models.CharField(verbose_name="卡密",max_length=10)
    cost = models.DecimalField(max_digits=8,decimal_places=2,verbose_name="价格",default=0)
    proxy_man = models.ForeignKey(User,verbose_name="代理",null=True)
    used = models.BooleanField(verbose_name="是否使用过",default=False)
    deal_object = models.ForeignKey(Deal_record,verbose_name="交易对象",null=True)
    begin_time = models.DateTimeField(verbose_name="创卡时间",default=timezone.now)

    def __str__(self):
        return "卡密："+ self.code +"--是否使用："+ str(self.used)+"----请尽量不要用管理员网页创建或使用授权码！"

class Notice(models.Model):
    admin_object = models.ForeignKey(User,verbose_name="管理员")
    time = models.DateField(verbose_name="创建时间",auto_now_add=True)
    title = models.CharField(verbose_name="标题",max_length=30)
    word = models.CharField(verbose_name="内容",max_length=1024)

class Question(models.Model):
    user_object = models.ForeignKey(User,verbose_name="用户")
    question_word = models.CharField(verbose_name="工单内容",max_length=1024)
    time = models.DateField(verbose_name="创建时间",auto_now_add=True)
    state = models.BooleanField(verbose_name="工单状态",default=True) #工单关闭代表管理员已经检查过。



def get_Code(num=15): #获取随机TOKEN，通过传入位数。
    while 1:
        a = "1234567890"
        b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sa = []
        for i in range(num//2):
            sa.append(random.choice(b))
            sa.append(random.choice(a))
        sa = "".join(sa)
        try:
            Time_code.objects.get(code=sa)
        except Time_code.DoesNotExist:
            return sa
def get_deal_code(num=5): #获取随机TOKEN，通过传入位数。
    while 1:
        a = "1234567890"
        sa = []
        for i in range(num):
            sa.append(random.choice(a))
        sa = "".join(sa)
        try:
            Deal_record.objects.get(deal_code=sa)
        except Deal_record.DoesNotExist:
            return sa
