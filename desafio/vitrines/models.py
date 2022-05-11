from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    state = models.CharField(max_length=2)

    def __str__(self):
        return self.name
    
    '''def all_json(self):
        return [x.dados_json() for x in c if x != None] '''

    def dados_json(self):
        return {"name": self.name, "slug": self.slug, "state": self.state}


class Country(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)


class Itens(models.Model):
    hotel_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.CharField(max_length=1024)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=19, decimal_places=2)


class Page(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    itens = models.ForeignKey(Itens, on_delete=models.CASCADE)
