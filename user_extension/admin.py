from django.contrib import admin
from user_extension.models import User


# Register your models here.
@admin.register(User)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'first_name',
        'phone',
    )
    list_display_links = (
        'id',
        'username',
        'first_name',
        'phone',
    )
