from django.db import models

# Create your models here.
from sorl.thumbnail import ImageField


class AllServices(models.Model):
    heading = models.CharField(max_length=50, verbose_name='Название услуги')
    heading_min = models.CharField(max_length=100, verbose_name='Минимальное описание (100 сим)')
    heading_max = models.CharField(max_length=1000, verbose_name='Полное описание услуги')
    img = ImageField(upload_to='allservices/img/%Y/%m/%d/')
