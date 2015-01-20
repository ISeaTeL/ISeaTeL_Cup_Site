# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sudo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('schedule', models.TextField()),
                ('time', models.DateTimeField(default=datetime.datetime(2015, 1, 20, 20, 57, 28, 765573), auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
