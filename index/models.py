from django.db import models
from datetime import datetime

# Create your models here.
class Bulletin(models.Model):
    content = models.TextField()
    title = models.TextField()
    time = models.DateTimeField(default=datetime.now(), editable=False, auto_now_add=True)
    def __unicode__(self):
        return 'title: ' + self.title + ' | content: ' + self.content + ' @' + str(self.time.date())

class Visited(models.Model):
    hits = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.hits)
