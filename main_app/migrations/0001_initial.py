# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_code',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(verbose_name='API用密链', max_length=50, default='test')),
            ],
        ),
        migrations.CreateModel(
            name='Authorization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('customer_QQ', models.PositiveIntegerField(verbose_name='客户的QQ')),
                ('bot_QQ', models.PositiveIntegerField(verbose_name='机器人的QQ')),
                ('begin_time', models.DateField(verbose_name='创建时间', auto_now_add=True)),
                ('deadline_time', models.DateField(verbose_name='到期时间', default=django.utils.timezone.now)),
                ('proxy_man', models.ForeignKey(verbose_name='代理', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Others_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('balance', models.PositiveIntegerField(verbose_name='用户余额', default=0)),
                ('ad', models.CharField(verbose_name='代理广告', max_length=30)),
                ('TOKEN', models.CharField(verbose_name='API密链', max_length=15, unique=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('software_id', models.PositiveIntegerField(verbose_name='软件ID', unique=True)),
                ('software_name', models.CharField(verbose_name='软件名', max_length=30)),
                ('software_version_number', models.CharField(verbose_name='软件版本号', max_length=30, default='V1.0')),
                ('software_each_time', models.PositiveIntegerField(verbose_name='套餐时间（按小时计算）', default=720)),
                ('software_cost', models.PositiveIntegerField(verbose_name='套餐价格', default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Time_code',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('time', models.PositiveIntegerField(verbose_name='时长')),
                ('code', models.CharField(verbose_name='卡密', max_length=10)),
                ('cost', models.PositiveIntegerField(verbose_name='价格')),
                ('used', models.BooleanField(verbose_name='是否使用过', default=False)),
                ('proxy_man', models.ForeignKey(verbose_name='代理', null=True, to=settings.AUTH_USER_MODEL)),
                ('software', models.ForeignKey(verbose_name='软件对象', to='main_app.Software')),
            ],
        ),
        migrations.AddField(
            model_name='authorization',
            name='software',
            field=models.ForeignKey(verbose_name='软件对象', to='main_app.Software'),
        ),
    ]
