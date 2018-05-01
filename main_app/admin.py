from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

admin.site.register(software)
admin.site.register(authorization)
admin.site.register(time_code)

# Register your models here.
