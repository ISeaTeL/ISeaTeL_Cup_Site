# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clarification', '0008_auto_20141127_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='clarification',
            name='asker',
            field=models.TextField(default=b'Anonymous'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 27, 17, 4, 11, 404235), auto_now=True),
        ),
        migrations.AlterField(
            model_name='clarification',
            name='reply',
            field=models.TextField(default=b'Not yet reply.'),
        ),
        migrations.AlterField(
            model_name='clarification',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 27, 17, 4, 11, 405129), auto_now=True),
        ),
    ]
