from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.db import models
from django.utils import timezone

from django.utils.datetime_safe import datetime, date

from all_services.models import AllServices

User = get_user_model()


class Zapis(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Имя')
    message = models.TextField(max_length=200, verbose_name='Сообщение')
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    desired_time = models.DateTimeField(default=timezone.now, verbose_name='Желаемая дата')
    # desired_data = models.DateField(default=date.today, verbose_name='Желаемая дата')
    service = models.ForeignKey(AllServices, on_delete=models.CASCADE, verbose_name='Желаемый сервис')
    car = models.CharField(max_length=100, verbose_name='Автобомиль')
    YEAR_CHOICES = []
    for r in range(1980, (datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.now().year, verbose_name='Год авто')

    def __str__(self):
        # Здесь возвращаем строку с именем и фамилией
        return '{0}'.format(self.name, )

    class Meta:
        verbose_name = 'Запись на ремонт'
        verbose_name_plural = 'Записи на ремонт'


