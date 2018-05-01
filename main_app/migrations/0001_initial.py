# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='authorization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('customer_QQ', models.PositiveIntegerField(verbose_name='客户的QQ')),
                ('bot_QQ', models.PositiveIntegerField(verbose_name='机器人的QQ')),
                ('begin_time', models.DateField(verbose_name='创建时间', auto_now_add=True)),
                ('deadline_time', models.DateField(verbose_name='到期时间', auto_now_add=True)),
                ('proxy_man', models.ForeignKey(verbose_name='代理', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='software',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('software_id', models.PositiveIntegerField(verbose_name='软件ID', unique=True)),
                ('software_name', models.CharField(verbose_name='软件名', max_length=30)),
                ('software_version_number', models.CharField(verbose_name='软件版本号', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='time_code',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('time', models.PositiveIntegerField(verbose_name='时长')),
                ('code', models.CharField(verbose_name='卡密', max_length=10)),
                ('cost', models.PositiveIntegerField(verbose_name='价格')),
                ('software', models.ForeignKey(verbose_name='软件对象', to='main_app.software')),
            ],
        ),
        migrations.AddField(
            model_name='authorization',
            name='software',
            field=models.ForeignKey(verbose_name='软件对象', to='main_app.software'),
        ),
    ]
