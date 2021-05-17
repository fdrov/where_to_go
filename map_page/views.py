from django.shortcuts import render


def main_page(request):
    return render(request, 'map_page/index.html')