# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clarification', '0012_auto_20141128_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletin',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 28, 5, 22, 16, 299084), auto_now=True),
        ),
        migrations.AlterField(
            model_name='clarification',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 28, 5, 22, 16, 300804), auto_now=True),
        ),
    ]
