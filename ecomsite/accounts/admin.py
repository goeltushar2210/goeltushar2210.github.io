from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import UserAdminCreationForm,UserAdminChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

User = get_user_model()



class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('first_name','email', 'admin')
    list_filter = ('admin','staff','active')      # Filter
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('first_name', {'fields': ('first_name',)}),
        ('last_name', {'fields': ('last_name',)}),
        ('Permissions', {'fields': ('admin','staff','active')}),    #permissions
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email','first_name','last_name',)
    ordering = ('email',)
    filter_horizontal = ()




class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','phone','address','city','country']



admin.site.register(UserProfile,UserProfileAdmin)     
admin.site.register(User, UserAdmin)

