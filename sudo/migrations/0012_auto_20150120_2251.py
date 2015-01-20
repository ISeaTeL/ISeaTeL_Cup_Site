# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sudo', '0011_auto_20150120_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sudo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 20, 22, 51, 5, 281157), auto_now_add=True),
            preserve_default=True,
        ),
    ]
