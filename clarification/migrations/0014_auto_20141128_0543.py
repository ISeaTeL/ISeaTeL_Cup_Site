# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clarification', '0013_auto_20141128_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletin',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 28, 5, 43, 9, 364895), auto_now=True),
        ),
        migrations.AlterField(
            model_name='clarification',
            name='reply',
            field=models.TextField(default=b'No reply yet.'),
        ),
        migrations.AlterField(
            model_name='clarification',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 28, 5, 43, 9, 365420), auto_now=True),
        ),
    ]
