# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sudo', '0004_auto_20150121_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sudo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 24, 16, 18, 38, 720043), auto_now_add=True),
            preserve_default=True,
        ),
    ]
