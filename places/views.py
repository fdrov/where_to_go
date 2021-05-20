from django.shortcuts import render

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
