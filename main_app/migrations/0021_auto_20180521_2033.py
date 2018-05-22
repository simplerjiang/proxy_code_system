# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_auto_20180521_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal_record',
            name='money',
            field=models.DecimalField(verbose_name='交易金额', default=0, max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='software',
            name='software_cost',
            field=models.DecimalField(verbose_name='用户余额', default=0, max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='time_code',
            name='cost',
            field=models.DecimalField(verbose_name='价格', default=0, max_digits=8, decimal_places=2),
        ),
    ]
