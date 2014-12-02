# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0002_remove_clarification_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='clarification',
            field=models.ForeignKey(default=123, to='contest.Clarification'),
            preserve_default=False,
        ),
    ]
