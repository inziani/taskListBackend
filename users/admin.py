from django.contrib import admin
from django.contrib.auth import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.base_user import BaseUserManager


from .models import User, UserProfile
from .forms import CustomUserCreationForm, CustomUserChangeForm



# Register your models here.

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete=False
    verbose_plural_name="User Profile"
    fk_name = 'user' 

class CustomUserAdmin(UserAdmin):
    model = User
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    
   

    list_display_links = ['email']
    search_fields = ('email',)
    ordering = ('email',)
    inlines = (UserProfileInline,)
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser',)
    list_filter = ('email', 'is_staff', 'is_active', 'is_superuser',)

    add_fieldsets = UserAdmin.add_fieldsets + (
    ('Personal Information',
    {'fields':(
      'email',
      ('name')
      , 'username',)
      }),
     )

    # fieldsets = UserAdmin.fieldsets + (
    # ('Personal Information', 
    # {'fields':(
    #     'username', 'email','name',
    #     )
    #     }),
    # )
    search_fields = ('email', 'username')
    ordering = ['email']
    filter_horizontal = ()

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.register(User, CustomUserAdmin)
