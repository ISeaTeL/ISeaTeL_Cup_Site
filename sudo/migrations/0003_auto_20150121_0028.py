# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sudo', '0002_auto_20150121_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sudo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 21, 0, 28, 49, 831934), auto_now_add=True),
            preserve_default=True,
        ),
    ]
