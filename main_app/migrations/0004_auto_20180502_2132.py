# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20180501_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='time_code',
            name='used',
            field=models.BooleanField(verbose_name='是否使用过', default=False),
        ),
        migrations.AlterField(
            model_name='admin_code',
            name='code',
            field=models.CharField(verbose_name='API用密链', max_length=50, default='M6S9A9r9J0P5Z8'),
        ),
        migrations.AlterField(
            model_name='time_code',
            name='software',
            field=models.ForeignKey(verbose_name='软件对象', to='main_app.Software'),
        ),
    ]
