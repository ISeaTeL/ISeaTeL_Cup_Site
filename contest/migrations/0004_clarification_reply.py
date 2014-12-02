# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0003_contest_clarification'),
    ]

    operations = [
        migrations.AddField(
            model_name='clarification',
            name='reply',
            field=models.TextField(default=123),
            preserve_default=False,
        ),
    ]
