from django.urls import path, re_path
from . import views


urlpatterns = [
    # ex: /vitrines/
    path('', views.index, name='index'),
    # ex: /vitrines/home/
    re_path('home/', views.home, name='home'),
    # ex: /vitrines/destinos/
    path('destinos/', views.destinos, name='destinos'),
    # ex: /vitrines/sobre/
    path('sobre/<category>/<country>/<state>/<city>/<item>/<page>',
         views.sobre, name='sobre'),
]
