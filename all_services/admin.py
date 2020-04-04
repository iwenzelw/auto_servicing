from django.contrib import admin

# Register your models here.
from all_services.models import AllServices


@admin.register(AllServices)
class AllServicesAdmin(admin.ModelAdmin):
    list_display = (
        'heading',
    )
    list_display_links = (
        'heading',
    )