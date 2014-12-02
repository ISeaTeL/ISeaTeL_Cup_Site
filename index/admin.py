from django.contrib import admin

# Register your models here.

from index.models import Bulletin, Visited

admin.site.register(Bulletin)
admin.site.register(Visited)
