from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import Place


def main_page(request):
    places = Place.objects.all()
    features = []
    for place in places:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": 'static/places/moscow_legends.json'

            }
        })
    context = {
        'data': {
            "type": "FeatureCollection",
            "features": features
        }
    }
    return render(request, 'map_page/index.html', context=context)


def place_details(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    data = {
        "title": place.title,
        "imgs": [image.img.url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lon
        }
    }
    return JsonResponse(data,
                        safe=False,
                        json_dumps_params={'ensure_ascii': False, 'indent': 2})
