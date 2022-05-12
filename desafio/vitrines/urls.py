from django.urls import path
from . import views


urlpatterns = [
    # ex: /vitrines/
    path('', views.index, name='index'),
    # ex: /vitrines/5/
    path('<page_id>/', views.page, name='page'),
    # ex: /vitrines/43/destinos/
    path('<city_id>/destinos/', views.destinos, name='destinos'),
    # ex: /vitrines/5/sobre/
    path('<item_id>/sobre/', views.sobre, name='sobre'),
]
