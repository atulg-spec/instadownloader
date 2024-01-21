from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'first_name', 'phone_number', 'is_active', 'is_staff')
    list_filter = ('is_staff', 'is_active')
    readonly_fields = ('access_token',)
    search_fields = ('email', 'first_name', 'last_name', 'phone_number')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password','access_token')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone_number', 'password1', 'password2'),
        }),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        return formfield
    
admin.site.register(CustomUser, CustomUserAdmin)

    
admin.site.site_header = "Digital Marketing"
admin.site.site_title = "Digital Marketing"
admin.site.index_title = " | Admin"
admin.site.unregister(Group)