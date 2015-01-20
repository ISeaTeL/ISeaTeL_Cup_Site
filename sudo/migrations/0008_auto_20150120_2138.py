# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sudo', '0007_auto_20150120_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='sudo',
            name='url_hash',
            field=models.TextField(default='123'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sudo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 20, 21, 37, 41, 490133), auto_now_add=True),
            preserve_default=True,
        ),
    ]
