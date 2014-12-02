# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0012_auto_20141202_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clarification',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 2, 23, 55, 44, 974798), auto_now_add=True),
            preserve_default=True,
        ),
    ]
