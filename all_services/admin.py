from django.contrib import admin
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget

from all_services.models import AllServices, ServiceSingle


class AllServicesForm(ModelForm):
    model = AllServices
    fields = '__all__'

    class Meta:
        widgets = {
            'heading_min': SummernoteWidget(),
            'heading_max': SummernoteWidget(),
        }


class ServiceSingleForm(ModelForm):
    model = ServiceSingle
    fields = '__all__'

    class Meta:
        widgets = {
            'title': SummernoteWidget(),

        }


@admin.register(AllServices)
class AllServicesAdmin(admin.ModelAdmin):
    form = AllServicesForm
    list_display = (
        'id',
        'heading',
        'get_image'
    )
    list_display_links = (
        'heading',
    )
    readonly_fields = ('get_image',)


@admin.register(ServiceSingle)
class ServiceSingleAdmin(admin.ModelAdmin):
    form = ServiceSingleForm
    list_display = (
        'id',
        'name',
        'get_image'
    )
    list_display_links = (
        'name',
    )
    readonly_fields = ('get_image',)
