from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView

from all_services.models import AllServices, ServiceSingle
from main.mixins import ListViewsMixin, DetailViewsMixin


class ServiceSingleList(ListView, ListViewsMixin):
    """ представление списка все оерации услуги """
    model = ServiceSingle
    template_name = 'all_services/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ServiceSingleList, self).get_context_data(**kwargs)
        context['title'] = 'Все операции'
        return context


class AllServiceList(ListView, ListViewsMixin):
    """ представление списка все сервисов-услуг """
    model = AllServices
    template_name = 'all_services/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AllServiceList, self).get_context_data(**kwargs)
        context['title'] = 'Все услуги'

        return context


class AllServiceDetail(DetailView, DetailViewsMixin):
    """ представление обьекта из списка сервисов-услуг """
    model = AllServices
    template_name = 'all_services/detail.html'

    def get_context_data(self, **kwargs):
        context = super(AllServiceDetail, self).get_context_data(**kwargs)
        context['title'] = 'описание услуги'
        context['service_single'] = ServiceSingle.objects.filter(service=self.kwargs['pk'])
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(AllServices, pk=self.kwargs.get("pk"))


class ServiceSingleDetail(DetailView, DetailViewsMixin):
    pass
