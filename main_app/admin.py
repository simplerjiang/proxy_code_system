from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
admin.site.register(Admin_code)
admin.site.register(Software)
admin.site.register(Authorization)
admin.site.register(Time_code)
# Register your models here.
