from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    state = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    def dados_json(self):
        return {"id": self.id, "name": self.name, "slug": self.slug, "state": self.state}


class Country(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def dados_json(self):
        return {"id": self.id, "name": self.name, "slug": self.slug}


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def dados_json(self):
        return {"id": self.id, "name": self.name, "slug": self.slug}


class Item(models.Model):
    hotel_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    image = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    page = models.ForeignKey(
        "Page", on_delete=models.CASCADE, related_name='page')

    def __str__(self):
        return self.hotel_name

    def dados_json(self):
        return {"id": self.id, "hotel_name": self.hotel_name, "slug": self.slug, "image": self.image, "city": self.city, "country": self.country, "category": self.category, "price": self.price, "page": self.page}


class Page(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def dados_json(self):
        return {"id": self.id, "title": self.title, "subtitle": self.subtitle}
