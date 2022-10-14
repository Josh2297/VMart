from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("id","username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email",'gender')}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
        ('Extra Info',{'fields':('phone_no','home_address','additional_phone_no',\
            'state_of_origin','resident_state','profile_pic','services','location_of_del',\
            'transport_ques','partnership_status')}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("id","username", "email","password1", "password2","first_name", "last_name",'gender','phone_no','home_address',\
                'additional_phone_no','state_of_origin','resident_state','profile_pic','services','location_of_del','transport_ques','partnership_status'),
            },
        ),
    )
    list_display=('email','first_name','last_name')
    list_filter=('partnership_status','groups','location_of_del')
    search_fields=('first_name__startswith','phone_no__icontains','email__startswith')

# Register Models
admin.site.register(CustomUser,CustomUserAdmin)