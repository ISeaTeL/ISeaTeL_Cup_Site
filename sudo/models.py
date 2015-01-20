# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
# Create your models here.

class Choices(models.Model):
    description = models.CharField(max_length=300)
    def __unicode__(self):
        return self.description

class Sudo(models.Model):
    name = models.TextField()
    email = models.TextField(unique=True)
    schedule = models.TextField()
    choices = models.ManyToManyField(Choices)
    url_hash = models.TextField()
    time = models.DateTimeField(default=datetime.now(), editable=True, auto_now_add=True)
    def __unicode__(self):
        return '%s | %s' % (self.name, self.email)