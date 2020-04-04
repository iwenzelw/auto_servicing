from django.contrib import admin

# Register your models here.
from location_address.models import LocAddress, SocialContacts


@admin.register(LocAddress)
class LocAddressAdmin(admin.ModelAdmin):
    list_display = (
        'street',
        'home',
    )
    list_display_links = (
        'street',
        'home',
    )


@admin.register(SocialContacts)
class SocialContactsAdmin(admin.ModelAdmin):
    list_display = (
        'tel',
    )
    list_display_links = (
        'tel',
    )
