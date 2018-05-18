# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20180517_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal_record',
            name='deal_code',
            field=models.CharField(verbose_name='交易编号', max_length=5, default=''),
        ),
        migrations.AlterField(
            model_name='admin_code',
            name='code',
            field=models.CharField(verbose_name='API用密链', max_length=50, default='s6m0V1c0I7T0j6'),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='deadline_time',
            field=models.DateTimeField(verbose_name='到期时间', default=datetime.datetime(2018, 5, 18, 15, 58, 3, 551307)),
        ),
        migrations.AlterField(
            model_name='deal_record',
            name='notes',
            field=models.CharField(verbose_name='交易备注', max_length=30, default='无'),
        ),
        migrations.AlterField(
            model_name='others_info',
            name='TOKEN',
            field=models.CharField(verbose_name='API密链', max_length=15, unique=True, default='i8b5z3a0H3d9X3'),
        ),
    ]
