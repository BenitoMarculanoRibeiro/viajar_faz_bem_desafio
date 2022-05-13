from django.shortcuts import render
from .models import *
pages = Page.objects.all()


def index(request):
    itens = Item.objects.all()
    return render(request, 'vitrines/index.html', {'itens': itens, 'pages': pages})


def home(request):
    page_id = 2
    itens = Item.objects.filter(page_id=page_id)
    return render(request, 'vitrines/index.html', {'itens': itens, 'pages': pages.filter(id=page_id)})


def destinos(request):
    page_id = 1
    itens = Item.objects.filter(page_id=page_id)
    return render(request, 'vitrines/index.html', {'itens': itens, 'pages': pages.filter(id=page_id)})


def sobre(request):
    page_id = 3
    itens = Item.objects.filter(page_id=page_id)
    return render(request, 'vitrines/index.html', {'itens': itens, 'pages': pages.filter(id=page_id)})
