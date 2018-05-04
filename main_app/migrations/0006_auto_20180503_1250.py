# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0005_auto_20180503_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Others_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('balance', models.PositiveIntegerField(verbose_name='用户余额', default=0)),
                ('ad', models.CharField(verbose_name='代理广告', max_length=30)),
                ('TOKEN', models.CharField(verbose_name='API密链', max_length=15, default='w4I1X5v0a7o5O6')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='admin_code',
            name='code',
            field=models.CharField(verbose_name='API用密链', max_length=50, default='X9z7e7a6Y8I7R5'),
        ),
        migrations.AlterField(
            model_name='time_code',
            name='software',
            field=models.ForeignKey(verbose_name='软件对象', to='main_app.Software'),
        ),
    ]
