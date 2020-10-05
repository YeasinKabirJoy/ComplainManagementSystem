from django.contrib import admin
from .models import Complain, Comment

# Register your models here.
admin.site.register([Complain, Comment])
