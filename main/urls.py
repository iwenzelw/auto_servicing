from django.urls import path
from . import views
from .views import MainView

app_name = 'main'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
]
