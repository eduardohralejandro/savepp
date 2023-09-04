from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ExtendedUser, Bill, Transaction, Category


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
admin.site.register(Bill)
admin.site.register(Transaction)
admin.site.register(Category)
