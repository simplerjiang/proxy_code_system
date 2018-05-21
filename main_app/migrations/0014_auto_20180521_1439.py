# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_auto_20180521_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='others_info',
            name='level',
            field=models.PositiveIntegerField(verbose_name='级别', default=1),
        ),
        migrations.AddField(
            model_name='others_info',
            name='up_proxy',
            field=models.PositiveIntegerField(verbose_name='上级', null=True),
        ),
        migrations.AlterField(
            model_name='admin_code',
            name='code',
            field=models.CharField(verbose_name='API用密链', max_length=50, default='M7s5j4m3D8E8i7'),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='deadline_time',
            field=models.DateTimeField(verbose_name='到期时间', default=datetime.datetime(2018, 5, 21, 14, 39, 27, 949222)),
        ),
        migrations.AlterField(
            model_name='others_info',
            name='TOKEN',
            field=models.CharField(verbose_name='API密链', max_length=15, unique=True, default='n9z0P7o7I5o7r3'),
        ),
        migrations.AlterField(
            model_name='time_code',
            name='begin_time',
            field=models.DateTimeField(verbose_name='创卡时间', default=datetime.datetime(2018, 5, 21, 14, 39, 27, 949222)),
        ),
    ]
