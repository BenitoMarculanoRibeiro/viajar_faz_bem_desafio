try:
    import manage
    manage.main()
except print(0):
    pass

from vitrines.models import City, Country, Category, Item, Page
import json


with open("files/all.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)


def insere_city(city):
    try:
        cidades = City.objects.filter(
            name=city['name'], slug=city['slug'], state=city['state'])
        if len(cidades) != 0:
            print(f'{city["name"]} Cadastrado')
            return cidades[0]
        else:
            print(f'Realizando Cadastro de {city["name"]}.')
            city = City(name=city['name'],
                        slug=city['slug'], state=city['state'])
            city.save()
            print('Cadastro Realizado')
            return city
    except Exception:
        return False


def insere_country(country):
    try:
        pais = Country.objects.filter(
            name=country['name'], slug=country['slug'])
        if len(pais) != 0:
            print(f'{country["name"]} Cadastrado')
            return pais[0]
        else:
            print(f'Realizando Cadastro de {country["name"]}.')
            country = Country(name=country['name'],
                              slug=country['slug'])
            country.save()
            print('Cadastro Realizado')
            return country
    except Exception:
        return False


def insere_category(category):
    try:
        categoria = Category.objects.filter(
            name=category['name'], slug=category['slug'])
        if len(categoria) != 0:
            print(f'{category["name"]} Cadastrado')
            print(categoria[0].id)
            return categoria[0]
        else:
            print(f'Realizando Cadastro de {category["name"]}.')
            category = Category(name=category['name'],
                                slug=category['slug'])
            category.save()
            print(category.id)
            print('Cadastro Realizado')
            return category
    except Exception:
        return False


def popula():
    for page in dados:
        print(page)
        paginas = Page.objects.filter(id=page["id"])
        if len(paginas) != 0:
            print(f'{page["title"]} Cadastrado')
            pagina = paginas[0]
        else:
            print(f'Realizando Cadastro de {page["title"]}.')
            pagina = Page(id=page["id"], title=page['title'],
                          subtitle=page['subtitle'])
            pagina.save()
            print('Cadastro Realizado')
        for item in page['itens']:
            city = insere_city(item['city'])
            country = insere_country(item['country'])
            category = insere_category(item['category'])
            print('i')
            print('\n')
            i = Item.objects.filter(hotel_name=item['hotel_name'], slug=item['slug'], image=item['image'], price=item['price'],
                                    city_id=city.id, country_id=country.id, category_id=category.id, page_id=pagina.id)
            print('\n')
            print('i')
            if len(i) != 0:
                print(f'{item["hotel_name"]} Cadastrado')
            else:
                print(f'Realizando Cadastro de {item["hotel_name"]}.')
                it = Item(hotel_name=item['hotel_name'], slug=item['slug'], image=item['image'], price=item['price'],
                          city_id=city.id, country_id=country.id, category_id=category.id, page_id=pagina.id)

                it.save()
                print('Cadastro Realizado')


popula()
