# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0006_auto_20180516_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal_record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('time', models.DateTimeField(verbose_name='交易时间', auto_now_add=True)),
                ('money', models.PositiveIntegerField(verbose_name='交易金额', default=0)),
                ('symbol', models.BooleanField(verbose_name='正负符号', default=True)),
                ('notes', models.CharField(verbose_name='交易备注', max_length=15, default='无')),
                ('acount', models.ForeignKey(verbose_name='交易账户', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='admin_code',
            name='code',
            field=models.CharField(verbose_name='API用密链', max_length=50, default='W1C0X3Z2a4J9x5'),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='deadline_time',
            field=models.DateTimeField(verbose_name='到期时间', default=datetime.datetime(2018, 5, 17, 21, 30, 15, 381832)),
        ),
        migrations.AlterField(
            model_name='others_info',
            name='TOKEN',
            field=models.CharField(verbose_name='API密链', max_length=15, unique=True, default='l6k0D1S3P2q9C4'),
        ),
        migrations.AlterField(
            model_name='others_info',
            name='ad',
            field=models.CharField(verbose_name='代理广告', max_length=30, default=''),
        ),
    ]
