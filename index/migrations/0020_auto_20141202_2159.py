# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0019_auto_20141202_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletin',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 2, 21, 59, 1, 952898), auto_now_add=True),
            preserve_default=True,
        ),
    ]
