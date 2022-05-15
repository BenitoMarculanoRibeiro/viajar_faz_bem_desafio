try:
    import manage
    manage.main()
except print(0):
    pass

from vitrines.models import *
import json
import requests
from lxml import html
xpath = "//img[contains(@src,'sbtur.com/')]"
images = []
page = requests.get('https://viajarfazbem.com/destinos/Brasil/RS/Canela')
tree = html.fromstring(page.content)

respostas = tree.xpath(xpath)

for resposta in respostas:
    images.append(resposta.attrib.get('src'))

page = requests.get('https://viajarfazbem.com/hoteis')
tree = html.fromstring(page.content)
respostas = tree.xpath(xpath)
for resposta in respostas:
    images.append(resposta.attrib.get('src'))


page_id = [2, 3]
itens = Item.objects.all()


for item in itens:
    item.image = images.pop(0)
    item.save()
