# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_auto_20180521_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='others_info',
            name='level',
            field=models.PositiveIntegerField(verbose_name='等级', default=1),
        ),
        migrations.AlterField(
            model_name='others_info',
            name='up_proxy',
            field=models.PositiveIntegerField(verbose_name='上级', default=1),
        ),
    ]
