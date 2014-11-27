# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clarification', '0004_remove_bulletin_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulletin',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 27, 16, 0, 0, 941025), auto_now=True),
            preserve_default=True,
        ),
    ]
