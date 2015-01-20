# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sudo', '0010_auto_20150120_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sudo',
            name='email',
            field=models.TextField(unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sudo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 20, 22, 49, 20, 594925), auto_now_add=True),
            preserve_default=True,
        ),
    ]
