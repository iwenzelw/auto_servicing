from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView

from location_address.models import LocAddress, SocialContacts


class MainView(TemplateView):
    # Представление главной страницы сайта
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location_address'] = LocAddress.objects.get()
        context['social_contacts'] = SocialContacts.objects.get()

        return context
