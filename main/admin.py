from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from main.models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'img',
    )

    list_display_links = (
        'id',
        'name',
    )

    # readonly_fields = ('get_image',)
    #
    # def get_image(self, obj):
    #     return mark_safe(f'<img src={obj.img.url} width="90" height="50"')
    #
    # get_image.short_description = "Изображение"

