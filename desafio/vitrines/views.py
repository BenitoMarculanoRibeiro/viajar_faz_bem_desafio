from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import *


def index(request):
    citys = City.objects.all()
    context = {'citys': citys}
    return render(request, 'vitrines/index.html', context)


def page(request, page_id):
    page = Page.objects.get(id=page_id)
    return HttpResponse(f"Pagina com a tematica sobre {page.title}.")


def destinos(request, city_id):
    city = City.objects.get(id=city_id)
    return HttpResponse(f"Pagina com hoteis da cidade {city}.")


def sobre(request, item_id):
    item = Item.objects.get(id=item_id)
    return HttpResponse(f"Pagina sobre o hotel {item.slug}.")
