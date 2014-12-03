from django.db import models
from datetime import datetime
# Create your models here.

class Clarification(models.Model):
    cid = models.IntegerField()
    asker = models.TextField(default='Anonymous')
    question = models.TextField()
    reply = models.TextField(default='No reply yet.')
    time = models.DateTimeField(default=datetime.now(), editable=True, auto_now_add=True)
    def __unicode__(self):
        return 'question: ' + self.question + ' | reply: ' + self.reply + ' @' + str(self.time.date())

class Contest(models.Model):
    cid = models.IntegerField()
    problem_url = models.TextField()
    solution_url = models.TextField()
    scoreboard_url = models.TextField()
    date = models.TextField()
    title = models.TextField()
    content = models.TextField()
    status = models.TextField()
    def __unicode__(self):
        return 'cid: ' + str(self.cid) + '| date: ' + self.date

