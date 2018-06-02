# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0026_auto_20180530_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='software_cost',
            field=models.DecimalField(verbose_name='软件价格', default=0, max_digits=8, decimal_places=2),
        ),
        migrations.AddField(
            model_name='software',
            name='software_each_time',
            field=models.PositiveIntegerField(verbose_name='套餐时间（按小时计算）', default=720),
        ),
    ]
