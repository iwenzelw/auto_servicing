from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView

from location_address.models import LocAddress, SocialContacts


class LocAddressView(TemplateView):
    template_name = 'address/index.html'
    # template_name = 'main/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location_address'] = LocAddress.objects.get()
        context['social_contacts'] = SocialContacts.objects.get()

        return context
