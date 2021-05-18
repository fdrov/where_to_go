from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    description_short = models.TextField(verbose_name='Сокращенное описание')
    description_long = models.TextField(verbose_name='Полное описание')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title
