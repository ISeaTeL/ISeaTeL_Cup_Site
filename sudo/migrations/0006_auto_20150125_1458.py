# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sudo', '0005_auto_20150124_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sudo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 25, 14, 58, 43, 139634), auto_now_add=True),
            preserve_default=True,
        ),
    ]
