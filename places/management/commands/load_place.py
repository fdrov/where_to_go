import os

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place


def load_place(url):
    response = requests.get(url)
    response.raise_for_status()
    raw_place = response.json()

    place, place_created = Place.objects.get_or_create(
        title=raw_place['title'],
        defaults={
            'description_short': raw_place['description_short'],
            'description_long': raw_place['description_long'],
            'lat': raw_place['coordinates']['lat'],
            'lon': raw_place['coordinates']['lng']},
    )
    if place_created:
        print(f'Добавляю место {raw_place["title"]}')
    else:
        print(f'Место {raw_place["title"]} уже добавлено')
        return
    for position, pic_url in enumerate(raw_place['imgs']):
        response = requests.get(pic_url)
        response.raise_for_status()

        img = ContentFile(response.content)

        image_field, image_created = place.images.get_or_create(
            position=position)
        if image_created:
            print(f'Добавляю фото {os.path.basename(pic_url)}')
            image_field.img.save(os.path.basename(pic_url), img, save=True)
        else:
            print(f'Фото {os.path.basename(pic_url)} уже есть')


class Command(BaseCommand):
    help = "Loads place details into the database"

    def add_arguments(self, parser):
        parser.add_argument('place_url', nargs='+', type=str)

    def handle(self, *args, **options):
        for url in options['place_url']:
            try:
                load_place(url)
            except requests.exceptions.RequestException:
                print(f'\nВозникла ошибка с адресом {url} \n')
                continue
