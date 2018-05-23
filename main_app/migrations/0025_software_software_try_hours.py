# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0024_auto_20180523_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='software_try_hours',
            field=models.PositiveIntegerField(verbose_name='试用时长', default=0),
        ),
    ]
