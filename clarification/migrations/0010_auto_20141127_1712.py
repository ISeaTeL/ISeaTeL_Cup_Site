# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clarification', '0009_auto_20141127_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletin',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 27, 17, 12, 52, 634866), auto_now=True),
        ),
        migrations.AlterField(
            model_name='clarification',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 27, 17, 12, 52, 635391), auto_now=True),
        ),
    ]
