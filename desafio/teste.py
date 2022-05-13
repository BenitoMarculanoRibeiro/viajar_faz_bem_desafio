try:
    import manage
    manage.main()
except print(0):
    pass

from vitrines.models import City, Country, Category, Item, Page
import json


itens  = Item.objects.all()
for i in itens:
    print(i.page_id)
pages = Page.objects.all()
print(pages.filter(id=1))