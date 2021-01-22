from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime


class StatusUser(models.Model):
    """
    ТЕКСТ
    :param models.Model - ТЕКСТ
    """
    status = models.CharField(verbose_name="Имя", max_length=64, unique=True)


class User(AbstractUser):
    """
    ТЕКСТ
    :param AbstractUser - ТЕКСТ
    """
    username = models.CharField(verbose_name="Логин", max_length=64, unique=True)
    name = models.CharField(verbose_name="Имя", max_length=64, default='')
    surname = models.CharField(verbose_name="Фамилия", max_length=64, default='')
    status = models.ForeignKey(StatusUser, on_delete=models.CASCADE, verbose_name="Статус", default=1)
    status_update = models.DateField(verbose_name="Дата смены статуса", default=datetime.date.today)
    date_create = models.DateField(verbose_name="Дата создания", default=datetime.date.today)
    date_update = models.DateField(verbose_name="Дата редактирования", default=datetime.date.today)
