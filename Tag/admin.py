from django.contrib import admin
from .models import Tag, ComplainTag


# Register your models here.
admin.site.register([Tag, ComplainTag])
