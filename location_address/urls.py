from django.urls import path
from . import views
from .views import LocAddressView

app_name = 'address'

urlpatterns = [
    path('location_address/', LocAddressView.as_view(), name='address'),
]
