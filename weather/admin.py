from django.contrib import admin

from .models import Weather, Summary


# models admin site registeration
admin.site.register(Weather)
admin.site.register(Summary)