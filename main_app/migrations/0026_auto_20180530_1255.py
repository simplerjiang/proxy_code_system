# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0025_software_software_try_hours'),
    ]

    operations = [
        migrations.CreateModel(
            name='Software_cost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('software_each_time', models.PositiveIntegerField(verbose_name='套餐时间（按小时计算）', default=720)),
                ('software_cost', models.DecimalField(verbose_name='软件价格', default=0, max_digits=8, decimal_places=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='software',
            name='software_cost',
        ),
        migrations.RemoveField(
            model_name='software',
            name='software_each_time',
        ),
        migrations.AddField(
            model_name='software_cost',
            name='software',
            field=models.ForeignKey(verbose_name='软件对象', to='main_app.Software'),
        ),
    ]
