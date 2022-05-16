from django.shortcuts import render
from .models import *


pages = Page.objects.all()


def index(request):
    itens = Item.objects.all()
    return render(request, 'vitrines/index.html', {'itens': itens, 'pages': pages})


def home(request):
    page_id = [2, 3]
    itens = Item.objects.filter(page_id__in=page_id)
    return render(request, 'vitrines/index.html', {'itens': itens, 'pages': pages.filter(id__in=page_id)})


def sobre(request, category, country, state, city, item, page):
    page_id = 3
    item = Item.objects.get(page_id=page, slug=item, city_id=City.objects.get(slug=city, state=state).id, country_id=Country.objects.get(
        slug=country).id, category_id=Category.objects.get(slug=category).id)
    itens = Item.objects.filter(page_id=page_id)
    return render(request, 'vitrines/sobre.html', {'item': item, 'itens': itens, 'pages': pages.filter(id=page_id)})


def destinos(request):
    res = request.GET
    try:
        text = res['text']
        city = Item.objects.filter(
            city__in=City.objects.filter(name__icontains=text))
        state = Item.objects.filter(
            city__in=City.objects.filter(state__icontains=text))
        category = Item.objects.filter(
            category__in=Category.objects.filter(name__icontains=text))
        country = Item.objects.filter(
            country__in=Country.objects.filter(name__icontains=text))
        hotel = Item.objects.filter(hotel_name__icontains=text)
        all = [city, state, category, country, hotel]
        itens = []
        [itens.extend(x) for x in all if x is not None]
    except Exception as e:
        text = None
        itens = Item.objects.all()

    try:
        state = res['state']
        if state != '':
            itens = [x for x in itens if x.city.state == state]
    except Exception as e:
        state = None
    itens = list(set(itens))
    try:
        limit = res['limit']
        itens = itens[:int(limit)]
    except Exception as e:
        limit = None
    return render(request, "vitrines/destinos.html", {'itens': itens, 'text': text, 'limit': limit, 'state': state, 'states': set([x['state'] for x in City.objects.values('state') if x is not None])})
