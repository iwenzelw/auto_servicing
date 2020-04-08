from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from all_services.models import AllServices


class AllServicesForm(ModelForm):
    class Meta:
        model = AllServices
        fields = '__all__'
        widgets = {
            'heading_min': SummernoteWidget(),
            'heading_max': SummernoteWidget(),
        }
