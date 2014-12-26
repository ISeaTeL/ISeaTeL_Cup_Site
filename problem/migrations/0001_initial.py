# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import problem.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('pid', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255, blank=True)),
                ('content', models.CharField(max_length=50000, blank=True)),
                ('input', models.FileField(storage=problem.models.OverwriteStorage(), upload_to=problem.models.in_file_name, blank=True)),
                ('output', models.FileField(storage=problem.models.OverwriteStorage(), upload_to=problem.models.out_file_name, blank=True)),
                ('time_limit', models.IntegerField(default=1, blank=True)),
                ('mem_limit', models.IntegerField(default=32000, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
