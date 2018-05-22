# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0005_auto_20180506_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('time', models.DateField(verbose_name='创建时间', auto_now_add=True)),
                ('title', models.CharField(verbose_name='标题', max_length=30)),
                ('word', models.CharField(verbose_name='内容', max_length=1024)),
                ('admin_object', models.ForeignKey(verbose_name='管理员', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('question_word', models.CharField(verbose_name='工单内容', max_length=1024)),
                ('time', models.DateField(verbose_name='创建时间', auto_now_add=True)),
                ('state', models.BooleanField(verbose_name='工单状态', default=True)),
                ('user_object', models.ForeignKey(verbose_name='用户', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='admin_code',
            name='code',
            field=models.CharField(verbose_name='API用密链', max_length=50, default='x7G4T2y8J3q8o3'),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='deadline_time',
            field=models.DateTimeField(verbose_name='到期时间', default=datetime.datetime(2018, 5, 16, 12, 4, 29, 199010)),
        ),
    ]
