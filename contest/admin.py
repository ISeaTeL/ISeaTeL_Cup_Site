from django.contrib import admin

# Register your models here.

from contest.models import *

admin.site.register(Contest)
admin.site.register(Clarification)
admin.site.register(SignUp)
admin.site.register(Feedback)
admin.site.register(Dictionary)
