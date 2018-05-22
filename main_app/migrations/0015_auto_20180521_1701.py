# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_auto_20180521_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_code',
            name='code',
            field=models.CharField(verbose_name='API用密链', max_length=50, default='E8D6v7I1b6c4L8'),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='deadline_time',
            field=models.DateTimeField(verbose_name='到期时间', default=datetime.datetime(2018, 5, 21, 17, 1, 48, 105220)),
        ),
        migrations.AlterField(
            model_name='others_info',
            name='TOKEN',
            field=models.CharField(verbose_name='API密链', max_length=15, unique=True, default='k1f2H7c5g8S7P6'),
        ),
        migrations.AlterField(
            model_name='time_code',
            name='begin_time',
            field=models.DateTimeField(verbose_name='创卡时间', default=datetime.datetime(2018, 5, 21, 17, 1, 48, 105220)),
        ),
    ]
