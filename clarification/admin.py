from django.contrib import admin

# Register your models here.

from clarification.models import Bulletin, Clarification

admin.site.register(Bulletin)

admin.site.register(Clarification)