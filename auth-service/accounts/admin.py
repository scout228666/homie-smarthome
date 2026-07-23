from django.contrib import admin
from accounts.models import User, Invite


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_active')
    search_fields = ('first_name',)
    list_filter = ('is_active',)

@admin.register(Invite)
class InviteAdmin(admin.ModelAdmin):
    list_display = ('code', 'is_active', 'created_at', 'used_by')
    list_filter = ('is_active',)
    search_fields = ('code',)
