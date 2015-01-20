# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JudgeResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sid', models.IntegerField()),
                ('pid', models.IntegerField()),
                ('username', models.CharField(max_length=50)),
                ('result', models.CharField(max_length=50)),
                ('time', models.IntegerField()),
                ('memory', models.IntegerField()),
                ('message', models.CharField(max_length=500)),
                ('status', models.IntegerField()),
                ('submit_time', models.DateTimeField(default=datetime.datetime(2015, 1, 21, 0, 30, 34, 354303), auto_now_add=True)),
                ('language', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
