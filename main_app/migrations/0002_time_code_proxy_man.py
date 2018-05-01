# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='time_code',
            name='proxy_man',
            field=models.ForeignKey(verbose_name='代理', null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
