# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clarification', '0007_auto_20141127_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clarification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField()),
                ('reply', models.TextField()),
                ('time', models.DateTimeField(default=datetime.datetime(2014, 11, 27, 17, 1, 3, 794031), auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 27, 17, 1, 3, 793485), auto_now=True),
        ),
    ]
