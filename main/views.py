from pprint import pprint

from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView

from all_services.models import AllServices
from location_address.models import LocAddress, SocialContacts
from main.mixins import ListViewsMixin


class MainView(TemplateView, ListViewsMixin):
    # Представление главной страницы сайта
    template_name = 'main/index.html'
    object_list = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
