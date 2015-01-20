# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sudo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sudo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 21, 0, 13, 5, 258119), auto_now_add=True),
            preserve_default=True,
        ),
    ]
