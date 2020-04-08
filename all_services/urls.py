from django.urls import path
from . import views
from .views import AllServiceList, AllServiceDetail, ServiceSingleList, ServiceSingleDetail

app_name = 'all_service'

urlpatterns = [
    path('all_service/service/list/', AllServiceList.as_view(), name='all_service-list'),
    path('all_service/service/detail/<int:pk>', AllServiceDetail.as_view(), name='all_service-detail'),
    path('all_service/service/single/list/', ServiceSingleList.as_view(), name='service_single-list'),
    path('all_service/service/single/detail/<int:pk>', ServiceSingleDetail.as_view(), name='service_single-detail'),
]
