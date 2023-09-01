from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ExtendedUser


class CustomUserAdmin(UserAdmin):
    readonly_fields = ["updated"]
    fieldsets = (
        *UserAdmin.fieldsets, (
            'Aditional Information',
            {
                'fields': ('avatar', 'phone', 'updated')
            }
        )
    )


admin.site.register(ExtendedUser, CustomUserAdmin)
