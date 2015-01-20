from django.contrib import admin

# Register your models here.

from sudo.models import *

admin.site.register(Sudo)
admin.site.register(Choices)