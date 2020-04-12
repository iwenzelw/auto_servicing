from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.BigIntegerField(verbose_name='Телефон', unique=True, blank=True, null=True)
    city = models.CharField(max_length=100, default='', blank=True)
