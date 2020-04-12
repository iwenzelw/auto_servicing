from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill


class Banner(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название банера')
    title = models.TextField(max_length=400, verbose_name='Техст На банере')
    img = ProcessedImageField(upload_to='banner/%Y/%m/%d/', blank=True,
                              processors=[ResizeToFill(1920, 720)],
                              format='webp',
                              options={'quality': 70}, verbose_name='Картинка')
    img_thumbnail = ImageSpecField(source='img',
                                   processors=[ResizeToFill(384, 144)],
                                   format='webp',
                                   options={'quality': 60})

    def get_image(self):
        if self.img:
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="60"/></a>'.format(self.img.url))
        else:
            return '(Нет изображения)'

    get_image.short_description = "Изображение"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Банер'
        verbose_name_plural = 'Банеры'
