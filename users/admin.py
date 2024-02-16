from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.shortcuts import redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin, admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = [
        'id',
        'first_name',
        'last_name',
        'email',
        'user_type',
        'tel_number',
    ]
    list_display_links = [
        'id',
        'first_name',
        'last_name',
        'email',
        'user_type',
        'tel_number',
    ]

    search_fields = [
        'id',
        'first_name',
        'last_name',
        'email',
        'user_type',
        'tel_number',
    ]
    list_per_page = 100

    fieldsets = [
        [
            'Personal Info',
            {
                "classes": ["wide", "extrapretty", ],
                'fields': [
                    'first_name',
                    'last_name',
                    'email',
                    'username',
                    'password',
                ],
            },
        ],
        [
            'Other info',
            {
                "classes": ["wide", "extrapretty", "collapse"],
                'fields': [
                    'user_type',
                    'tel_number',
                ],
            },
        ],
        [
            'Permissions',
            {
                "classes": ["wide", "extrapretty", "collapse"],
                'fields': [
                    'is_superuser',
                    'is_staff',
                    'is_active',
                    'groups',
                    'user_permissions',
                ],
            },
        ],
        [
            'Important dates',
            {
                "classes": ["wide", "extrapretty", "collapse"],
                'fields': [
                    'last_login',
                    'date_joined',
                ],
            },
        ],
    ]

    add_fieldsets = [
        [
            None,
            {
                "fields": [
                    'first_name',
                    'last_name',
                    'username',
                    'email',
                    'user_type',
                    'tel_number',
                    'password1',
                    'password2',
                ],
            },
        ],
    ]


admin.site.register(CustomUser, CustomUserAdmin)
