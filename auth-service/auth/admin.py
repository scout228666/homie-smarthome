from django.contrib import admin
from models import User


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'is_active')
    search_fields = ('first_name',)
    list_filter = ('is_active',)