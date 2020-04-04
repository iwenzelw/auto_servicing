from django.db import models


# модель Адресса расположения
class LocAddress(models.Model):
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    home = models.CharField(max_length=5, verbose_name='Дом')

    def __str__(self):
        return str(self.street)

    class Meta:
        verbose_name = 'Место расположения'
        verbose_name_plural = 'Место расположения'


class SocialContacts(models.Model):
    time = models.CharField(max_length=200, verbose_name='Время работы',)
    tel = models.CharField(max_length=100, verbose_name='Телефон')
    mail = models.EmailField(max_length=100, verbose_name='Mail', null=True, blank=True)
    vk = models.CharField(max_length=200, verbose_name='VK', null=True, blank=True)
    ok = models.CharField(max_length=200, verbose_name='OK', null=True, blank=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'