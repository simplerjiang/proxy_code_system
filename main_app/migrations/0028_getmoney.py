# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0027_auto_20180530_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Getmoney',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('time', models.DateTimeField(verbose_name='申请时间', auto_now_add=True)),
                ('money', models.PositiveIntegerField(verbose_name='提现金额', default=0)),
                ('money_account_name', models.CharField(verbose_name='提现账号种类', max_length=100)),
                ('money_account_num', models.CharField(verbose_name='提现账号', max_length=100)),
                ('flag', models.BooleanField(verbose_name='是否完成提现', default=False)),
                ('finished_time', models.DateTimeField(verbose_name='完成时间', auto_now=True)),
                ('proxy_account', models.ForeignKey(verbose_name='代理账号对象', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
