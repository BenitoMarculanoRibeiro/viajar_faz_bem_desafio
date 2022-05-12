from django.contrib import admin
from .models import *
'''admin.site.register(City)
admin.site.register(Country)
admin.site.register(Category)
admin.site.register(Itens)'''


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'state')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'hotel_name', 'slug', 'image', 'city',
                    'country', 'category', 'price', 'page')
    prepopulated_fields = {"slug": ("hotel_name",)}


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle')


'''




@admin.register(Itens)
class ItensAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created', 'updated')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created', 'updated')
    prepopulated_fields = {"slug": ("title",)}
'''
