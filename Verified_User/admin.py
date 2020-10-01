from django.contrib import admin
from .models import Verified_User,Verified_Email

# Register your models here.
admin.site.register([Verified_User,Verified_Email])
