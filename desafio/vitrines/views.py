from django.shortcuts import render
from .models import *
pages = Page.objects.all()


def index(request):
    itens = Item.objects.all()
    print(itens)
    return render(request, 'vitrines/index.html', {'itens': itens, 'pages': pages})


def home(request):
    page_id = [2, 3]
    itens = Item.objects.filter(page_id__in=page_id)
    return render(request, 'vitrines/index.html', {'itens': itens, 'pages': pages.filter(id__in=page_id)})


def destinos(request):
    page_id = 1
    itens = Item.objects.filter(page_id=page_id)
    return render(request, 'vitrines/index.html', {'itens': itens, 'pages': pages.filter(id=page_id)})


def sobre(request, category, country, state, city, item):
    page_id = 3
    print(category, country, state, city, item)
    print('\n')
    itens = Item.objects.filter(page_id=page_id)
    return render(request, 'vitrines/index.html', {'itens': itens, 'pages': pages.filter(id=page_id)})
