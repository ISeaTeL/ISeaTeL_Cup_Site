# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oj_judge', '0013_auto_20150120_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judgeresult',
            name='submit_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 20, 21, 43, 43, 128380), auto_now_add=True),
            preserve_default=True,
        ),
    ]