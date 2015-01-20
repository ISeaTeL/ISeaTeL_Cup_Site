# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sudo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('email', models.TextField(unique=True)),
                ('schedule', models.TextField()),
                ('url_hash', models.TextField()),
                ('time', models.DateTimeField(default=datetime.datetime(2015, 1, 21, 0, 12, 13, 390329), auto_now_add=True)),
                ('choices', models.ManyToManyField(to='sudo.Choices')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
