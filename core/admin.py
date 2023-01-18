from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', "first_name", 'last_name',)
    search_fields = ('email', 'first_name', "last_name", "username",)
    list_filter = ('is_staff', "is_active", "is_superuser",)
