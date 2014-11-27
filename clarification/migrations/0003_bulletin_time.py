# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clarification', '0002_bulletin_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulletin',
            name='time',
            field=models.DateTimeField(default=datetime.date(2014, 11, 27), auto_now=True),
            preserve_default=False,
        ),
    ]
