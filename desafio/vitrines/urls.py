from django.urls import path
from . import views


urlpatterns = [
    # ex: /vitrines/
    path('', views.index, name='index'),
    # ex: /vitrines/home/
    path('home/', views.home, name='home'),
    # ex: /vitrines/destinos/
    path('destinos/', views.destinos, name='destinos'),
    # ex: /vitrines/sobre/
    path('sobre/', views.sobre, name='sobre'),
]
