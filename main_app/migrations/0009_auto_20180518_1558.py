# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20180518_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_code',
            name='code',
            field=models.CharField(verbose_name='API用密链', max_length=50, default='u6T0M2B1N0w1o3'),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='deadline_time',
            field=models.DateTimeField(verbose_name='到期时间', default=datetime.datetime(2018, 5, 18, 15, 58, 16, 880771)),
        ),
        migrations.AlterField(
            model_name='deal_record',
            name='deal_code',
            field=models.CharField(verbose_name='交易编号', max_length=5, blank=True),
        ),
        migrations.AlterField(
            model_name='others_info',
            name='TOKEN',
            field=models.CharField(verbose_name='API密链', max_length=15, unique=True, default='d2Q2d0m7P5B8e2'),
        ),
    ]
