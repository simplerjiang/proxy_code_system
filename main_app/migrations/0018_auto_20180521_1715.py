# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_auto_20180521_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='others_info',
            name='level',
            field=models.CharField(verbose_name='等级', max_length=15, default='1'),
        ),
        migrations.AddField(
            model_name='others_info',
            name='up_proxy',
            field=models.CharField(verbose_name='上级', max_length=15, default='1'),
        ),
    ]
