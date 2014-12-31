from django.db import models
from datetime import datetime
class JudgeResult(models.Model):
    sid = models.IntegerField()
    pid = models.IntegerField()
    username = models.CharField(max_length=50)
    result = models.CharField(max_length=50)
    time = models.IntegerField()
    memory = models.IntegerField()
    message = models.CharField(max_length=500)
    status = models.IntegerField()
    submit_time = models.DateTimeField(default=datetime.now(), editable=True, auto_now_add=True)
    language = models.CharField(max_length=50)
    def __str__(self):
        return self.username + ': ' + self.result
    