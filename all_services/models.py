from django.db import models

# Create your models here.
from django.urls import reverse
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill


class AllServices(models.Model):
    heading = models.CharField(max_length=50, verbose_name='Название услуги')
    heading_min = models.TextField(max_length=200, verbose_name='Минимальное описание (100 сим)')
    heading_max = models.TextField(max_length=2000, verbose_name='Полное описание услуги')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовать?')
    # variant_1 = models.BooleanField(default=True, verbose_name='Опубликовать вариантом иконки?')
    variant_2 = models.BooleanField(default=True, verbose_name='Опубликовать вариантом картинки?')
    img = ProcessedImageField(upload_to='all_services/img/%Y/%m/%d/', blank=True,
                              processors=[ResizeToFill(800, 600)],
                              format='JPEG',
                              options={'quality': 80}, verbose_name='Картинка')
    img_thumbnail = ImageSpecField(source='img',
                                   processors=[ResizeToFill(390, 260)],
                                   format='JPEG',
                                   options={'quality': 60})

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def get_absolute_url_detail(self):  # переход для просмотра
        return reverse('all_service:all_service-detail', kwargs={'pk': self.pk})


class ServiceSingle(models.Model):
    service = models.ForeignKey(AllServices, on_delete=models.CASCADE, verbose_name='Услуга')
    name = models.CharField(max_length=200, verbose_name='название операции')
    title = models.TextField(max_length=2000, verbose_name='Описание операции')
    img = ProcessedImageField(upload_to='services_single/img/%Y/%m/%d/', blank=True,
                              processors=[ResizeToFill(800, 600)],
                              format='JPEG',
                              options={'quality': 80}, verbose_name='Картинка')
    img_thumbnail = ImageSpecField(source='img',
                                   processors=[ResizeToFill(390, 260)],
                                   format='JPEG',
                                   options={'quality': 60})

    class Meta:
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'

    def get_absolute_url_detail(self):  # переход для просмотра
        return reverse('all_service:service_single-detail', kwargs={'pk': self.pk})

