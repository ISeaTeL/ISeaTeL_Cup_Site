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
    cid = models.IntegerField(unique=True)
    problem_url = models.TextField()
    solution_url = models.TextField()
    scoreboard_url = models.TextField()
    signup_url = models.TextField()
    date = models.TextField()
    title = models.TextField()
    content = models.TextField()
    STATUS = (
        ('incoming', 'incoming'),
        ('running', 'running'),
        ('ended', 'ended'),
    )
    status = models.TextField(choices=STATUS)
    def __unicode__(self):
        return 'cid: ' + str(self.cid) + '| date: ' + self.date

class SignUp(models.Model):
    nthu_oj_id = models.TextField()
    name = models.TextField()
    email = models.TextField()
    message = models.TextField()
    time = models.DateTimeField(default=datetime.now(), editable=True, auto_now_add=True)
    def __unicode__(self):
        return 'nthu_oj_id: ' + str(self.nthu_oj_id) + '| time: ' + str(self.time)

