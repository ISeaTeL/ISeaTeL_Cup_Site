# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0008_auto_20141202_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clarification',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 2, 20, 13, 50, 874290), auto_now_add=True),
            preserve_default=True,
        ),
    ]
