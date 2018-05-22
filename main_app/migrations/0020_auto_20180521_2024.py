# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_auto_20180521_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='others_info',
            name='balance',
            field=models.DecimalField(verbose_name='用户余额', default=0, max_digits=8, decimal_places=2),
        ),
    ]
