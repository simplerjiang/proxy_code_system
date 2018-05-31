# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0028_getmoney'),
    ]

    operations = [
        migrations.AddField(
            model_name='getmoney',
            name='account_name',
            field=models.CharField(verbose_name='户主名', max_length=100, blank=True),
        ),
    ]
