# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oj_judge', '0004_auto_20150224_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judgeresult',
            name='submit_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 24, 21, 36, 49, 697840), auto_now_add=True),
            preserve_default=True,
        ),
    ]
