# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0005_auto_20141202_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contest',
            name='clarification',
        ),
        migrations.AddField(
            model_name='contest',
            name='cid',
            field=models.IntegerField(default=346),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clarification',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 2, 17, 14, 55, 398318), auto_now_add=True),
            preserve_default=True,
        ),
    ]
