# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20180503_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_code',
            name='code',
            field=models.CharField(verbose_name='API用密链', max_length=50, default='V4M1F0s1z8N8S8'),
        ),
        migrations.AlterField(
            model_name='others_info',
            name='TOKEN',
            field=models.CharField(verbose_name='API密链', max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='time_code',
            name='software',
            field=models.ForeignKey(verbose_name='软件对象', to='main_app.Software'),
        ),
    ]
