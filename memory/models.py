from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Memory(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='memory',
        verbose_name='Автор'
    )
    title = models.CharField(max_length=200, verbose_name='Название воспоминания')
    description = models.TextField(max_length=200, verbose_name='Описание')
    lat = models.FloatField(blank=True, null=True, verbose_name='Широта')
    lon = models.FloatField(blank=True, null=True, verbose_name='Долгота')
    created = models.DateTimeField('Дата добавления', auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Current_coord(models.Model):
    lat = models.FloatField(blank=True, null=True, verbose_name='Широта')
    lon = models.FloatField(blank=True, null=True, verbose_name='Долгота')
