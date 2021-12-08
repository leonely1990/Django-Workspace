from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_join', 'is_active')
    list_display_link = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_join')
    ordering = ('-date_join',)
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Register your models here.

admin.site.register(models.Account, AccountAdmin)