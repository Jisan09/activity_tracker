from django.contrib import admin
from .models import UserActivityLog
# Register your models here.


@admin.register(UserActivityLog)
class UserActivityLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'action', 'status', 'timestamp')
    list_filter = ('action', 'status', 'timestamp')
    search_fields = ('user__username', 'action', 'metadata')
    ordering = ('-timestamp',)
