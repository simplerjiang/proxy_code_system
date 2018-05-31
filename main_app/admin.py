from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from main_app.models import Others_info

admin.site.register(Admin_code)
admin.site.register(Authorization)
admin.site.register(Time_code)
admin.site.register(Software)
admin.site.register(Notice)
admin.site.register(Question)
admin.site.register(Deal_record)
admin.site.register(Getmoney)
# Register your models here.

class OtherInfoInline(admin.StackedInline):
    model = Others_info
    can_delete = False
    verbose_name_plural = '其他信息'

class UserAdmin(UserAdmin):
    inlines = (OtherInfoInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

