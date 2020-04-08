from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from all_services.forms import AllServicesForm
from all_services.models import AllServices, ServiceSingle


@admin.register(AllServices)
class AllServicesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'heading',
        'get_image'
    )
    list_display_links = (
        'heading',
    )
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.img.url} width="60" height="50"')

    get_image.short_description = "Изображение"


@admin.register(ServiceSingle)
class AllServicesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'get_image'
    )
    list_display_links = (
        'name',
    )
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.img.url} width="60" height="50"')

    get_image.short_description = "Изображение"
