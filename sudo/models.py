# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
# Create your models here.

class Sudo(models.Model):
    name = models.TextField()
    email = models.TextField()
    schedule = models.TextField()
    time = models.DateTimeField(default=datetime.now(), editable=True, auto_now_add=True)
    def __unicode__(self):
    	return '%s | %s' % (self.name, self.email)