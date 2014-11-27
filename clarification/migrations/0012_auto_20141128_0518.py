# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clarification', '0011_auto_20141127_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletin',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 28, 5, 18, 16, 855515), auto_now=True),
        ),
        migrations.AlterField(
            model_name='clarification',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 28, 5, 18, 16, 856055), auto_now=True),
        ),
    ]
