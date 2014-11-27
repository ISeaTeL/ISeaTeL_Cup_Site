from django.db import models
from datetime import datetime

# Create your models here.
class Bulletin(models.Model):
    content = models.TextField()
    title = models.TextField()
    time = models.DateTimeField(default=datetime.now(), auto_now=True)
    def __unicode__(self):
        return 'title: ' + self.title + ' | content: ' + self.content + ' @' + str(self.time.date())


class Clarification(models.Model):
    asker = models.TextField(default='Anonymous')
    question = models.TextField()
    reply = models.TextField(default='Not yet reply.')
    time = models.DateTimeField(default=datetime.now(), auto_now=True)
    def __unicode__(self):
        return 'question: ' + self.question + ' | reply: ' + self.reply + ' @' + str(self.time.date())
