# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0007_auto_20141202_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='clarification',
            name='cid',
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clarification',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 2, 17, 15, 53, 420045), auto_now_add=True),
            preserve_default=True,
        ),
    ]
