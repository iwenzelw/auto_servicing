from django.contrib import admin

# Register your models here.
from zapis_na_remont.models import Zapis


@admin.register(Zapis)
class ZapisAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'service',
        'car',
        'year',
        'data_create',
    )
    list_display_links = (
        'id',
        'name',
    )
