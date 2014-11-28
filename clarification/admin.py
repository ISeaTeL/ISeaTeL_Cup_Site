from django.contrib import admin

# Register your models here.

from clarification.models import Bulletin, Clarification, Visited

admin.site.register(Bulletin)

admin.site.register(Clarification)

admin.site.register(Visited)