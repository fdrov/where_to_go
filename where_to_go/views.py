from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def main_page(request):
    return render(request, 'index.html')
