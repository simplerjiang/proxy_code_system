# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_time_code_proxy_man'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_code',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(verbose_name='API用密链', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='authorization',
            name='software',
            field=models.ForeignKey(verbose_name='软件对象', to='main_app.Software'),
        ),
        migrations.AlterField(
            model_name='time_code',
            name='software',
            field=models.ForeignKey(verbose_name='软件对象', to='main_app.Software'),
        ),
    ]
