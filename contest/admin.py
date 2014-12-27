from django.contrib import admin

# Register your models here.

from contest.models import Contest, Clarification, SignUp, Dictionary

admin.site.register(Contest)
admin.site.register(Clarification)
admin.site.register(SignUp)
admin.site.register(Dictionary)
