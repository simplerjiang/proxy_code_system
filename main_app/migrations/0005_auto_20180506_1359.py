# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20180505_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_code',
            name='code',
            field=models.CharField(verbose_name='API用密链', max_length=50, default='n2Y0t7M1E2Y0m2'),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='deadline_time',
            field=models.DateTimeField(verbose_name='到期时间', default=datetime.datetime(2018, 5, 6, 13, 59, 19, 233547)),
        ),
    ]
