from django.contrib import admin

# Register your models here.
# user/admin.py
# from django.contrib import admin
from .models import UserLog, AdminLog

@admin.register(UserLog)
class UserLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp')
    search_fields = ('user__username', 'action')
    list_filter = ('timestamp',)

@admin.register(AdminLog)
class AdminLogAdmin(admin.ModelAdmin):
    list_display = ('admin', 'action', 'timestamp')
    search_fields = ('admin__username', 'action')
    list_filter = ('timestamp',)
