from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import MultipleObjectMixin

from all_services.models import AllServices
from location_address.models import LocAddress, SocialContacts


class DetailViewsMixin(SingleObjectMixin):

    def get_context_data(self, *args, **kwargs):
        context = super(DetailViewsMixin, self).get_context_data(**kwargs)
        context['location_address'] = LocAddress.objects.get()
        context['social_contacts'] = SocialContacts.objects.get()
        context['object_list'] = AllServices.objects.filter(is_published=True, variant_2=True)
        return context


class ListViewsMixin(MultipleObjectMixin):

    def get_context_data(self, *args, **kwargs):
        context = super(ListViewsMixin, self).get_context_data(*args, **kwargs)
        context['location_address'] = LocAddress.objects.get()
        context['social_contacts'] = SocialContacts.objects.get()
        context['object_list'] = AllServices.objects.filter(is_published=True, variant_2=True)
        return context
