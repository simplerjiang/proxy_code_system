# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20180518_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='time_code',
            name='deal_object',
            field=models.ForeignKey(verbose_name='交易对象', null=True, to='main_app.Deal_record'),
        ),
        migrations.AlterField(
            model_name='admin_code',
            name='code',
            field=models.CharField(verbose_name='API用密链', max_length=50, default='Y6E0s5v4L9p9b3'),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='deadline_time',
            field=models.DateTimeField(verbose_name='到期时间', default=datetime.datetime(2018, 5, 18, 16, 15, 11, 922597)),
        ),
        migrations.AlterField(
            model_name='deal_record',
            name='deal_code',
            field=models.CharField(verbose_name='交易编号', max_length=5),
        ),
        migrations.AlterField(
            model_name='deal_record',
            name='notes',
            field=models.CharField(verbose_name='交易备注', max_length=30, blank=True, default='无'),
        ),
        migrations.AlterField(
            model_name='others_info',
            name='TOKEN',
            field=models.CharField(verbose_name='API密链', max_length=15, unique=True, default='K3m6A1a9l9E5P8'),
        ),
    ]
