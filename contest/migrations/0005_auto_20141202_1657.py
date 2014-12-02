# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0004_clarification_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='clarification',
            name='asker',
            field=models.TextField(default=b'Anonymous'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clarification',
            name='question',
            field=models.TextField(default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clarification',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 2, 16, 57, 53, 95407), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='clarification',
            name='reply',
            field=models.TextField(default=b'No reply yet.'),
            preserve_default=True,
        ),
    ]
