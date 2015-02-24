# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sudo', '0007_auto_20150224_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='sudo',
            name='count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sudo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 24, 21, 36, 49, 701491), auto_now_add=True),
            preserve_default=True,
        ),
    ]
