from django.db import models

# Create your models here.
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill


class Banner(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название банера')
    title = models.TextField(max_length=400, verbose_name='Техст На банере')
    img = ProcessedImageField(upload_to='banner/%Y/%m/%d/', blank=True,
                              processors=[ResizeToFill(1920, 720)],
                              format='JPEG',
                              options={'quality': 80}, verbose_name='Картинка')
    img_thumbnail = ImageSpecField(source='img',
                                   processors=[ResizeToFill(384, 144)],
                                   format='JPEG',
                                   options={'quality': 60})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Банер'
        verbose_name_plural = 'Банеры'
