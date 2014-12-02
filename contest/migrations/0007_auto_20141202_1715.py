# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0006_auto_20141202_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clarification',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 2, 17, 15, 10, 816330), auto_now_add=True),
            preserve_default=True,
        ),
    ]
