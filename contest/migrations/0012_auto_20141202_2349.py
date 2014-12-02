# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0011_auto_20141202_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clarification',
            name='time',
            field=models.DateTimeField(verbose_name=b'default=datetime.now(), editable=True, auto_now_add=True'),
            preserve_default=True,
        ),
    ]
