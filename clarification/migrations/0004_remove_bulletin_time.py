# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clarification', '0003_bulletin_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bulletin',
            name='time',
        ),
    ]
