from django.db import models
from django.utils import timezone

class Request(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('waiting', 'Ожидает ответа'),
        ('resolved', 'Решена'),
    ]

    title = models.CharField(max_length=255, verbose_name="Название заявки")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания заявки")
    resolve_time_seconds = models.PositiveIntegerField(verbose_name="Время на решение в сек.")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new', verbose_name="Статус")

    def __str__(self):
        return self.title




# Create your models here.
