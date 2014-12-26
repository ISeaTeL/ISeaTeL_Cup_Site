from django.db import models
from django import forms
from django.forms import ModelForm
from pagedown.widgets import AdminPagedownWidget


from django.core.files.storage import FileSystemStorage
class OverwriteStorage(FileSystemStorage):
    def _save(self, name, content):
        if self.exists(name):
            self.delete(name)
        return super(OverwriteStorage, self)._save(name, content)

    def get_available_name(self, name):
        return name


def in_file_name(instance, filename):
    return '/'.join(['problem', str(instance.pid), 'in'])


def out_file_name(instance, filename):
    return '/'.join(['problem', str(instance.pid), 'out'])


# Create your models here.
class Problem(models.Model):
    pid = models.AutoField(primary_key=True)

    title = models.CharField(max_length=255,blank=True)
    content = models.CharField(max_length=50000,blank=True)
    
    input = models.FileField(upload_to=in_file_name, storage=OverwriteStorage(),blank=True)
    output = models.FileField(upload_to=out_file_name, storage=OverwriteStorage(),blank=True)

    time_limit = models.IntegerField(default=1,blank=True)
    mem_limit = models.IntegerField(default=32000,blank=True)
class ProblemForm(ModelForm):
    class Meta:
        model = Problem

    content = forms.CharField(max_length=10000,required=False,
        widget=AdminPagedownWidget())