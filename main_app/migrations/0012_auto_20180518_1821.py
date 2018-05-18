# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20180518_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='software_try',
            field=models.BooleanField(verbose_name='是否开启试用', default=False),
        ),
        migrations.AlterField(
            model_name='admin_code',
            name='code',
            field=models.CharField(verbose_name='API用密链', max_length=50, default='o9k0e6Y7Y3l8l0'),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='deadline_time',
            field=models.DateTimeField(verbose_name='到期时间', default=datetime.datetime(2018, 5, 18, 18, 21, 43, 157828)),
        ),
        migrations.AlterField(
            model_name='others_info',
            name='TOKEN',
            field=models.CharField(verbose_name='API密链', max_length=15, unique=True, default='V3W1t4s8O1o3O5'),
        ),
        migrations.AlterField(
            model_name='time_code',
            name='begin_time',
            field=models.DateTimeField(verbose_name='创卡时间', default=datetime.datetime(2018, 5, 18, 18, 21, 43, 157828)),
        ),
    ]
