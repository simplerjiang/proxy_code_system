# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0021_auto_20180521_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='others_info',
            name='up_proxy',
            field=models.PositiveIntegerField(verbose_name='上级（默认为0，代表没有上级）', default=0),
        ),
        migrations.AlterField(
            model_name='software',
            name='software_cost',
            field=models.DecimalField(verbose_name='软件价格', default=0, max_digits=8, decimal_places=2),
        ),
    ]
