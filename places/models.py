from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    description_short = models.TextField(verbose_name='Сокращенное описание')
    description_long = models.TextField(verbose_name='Полное описание')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place,
                              on_delete=models.CASCADE,
                              verbose_name='Место',
                              related_name='images')
    img = models.ImageField(verbose_name='Фото')
    position = models.PositiveSmallIntegerField(verbose_name='Позиция фото',
                                                default=0,
                                                blank=False,
                                                null=False)

    class Meta(object):
        ordering = ['position']

    def __str__(self):
        return f'{self.position}, {self.place}'
