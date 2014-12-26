from django.contrib import admin
from problem.models import *

# Register your models here.
class ProblemAdmin(admin.ModelAdmin):
    form = ProblemForm
    readonly_fields = ('pid',)
   

admin.site.register(Problem,ProblemAdmin)
