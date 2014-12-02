from django.contrib import admin

# Register your models here.

from contest.models import Contest, Clarification

admin.site.register(Contest)
admin.site.register(Clarification)
