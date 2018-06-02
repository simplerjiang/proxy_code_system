# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0025_software_software_try_hours'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='software',
            name='software_cost',
        ),
        migrations.RemoveField(
            model_name='software',
            name='software_each_time',
        ),
    ]
