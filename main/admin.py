from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from main.models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'get_image',
    )

    list_display_links = (
        'id',
        'name',
    )
