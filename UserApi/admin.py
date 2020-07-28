from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):

    list_display = ('email', 'username', 'phone', 'date_joined', 'is_active', 'is_staff', 'is_admin', 'is_superuser')
    list_filter = ('email', 'is_staff', 'is_active',)
    search_fields = ('email','username')

    filter_horizontal = ()
    list_filter = ()

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password', 'phone')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_admin', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_admin')}
        ),
    )
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)