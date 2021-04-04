import requests
import json
import lxml.html
from lxml import etree

TOKEN = '1673778119:AAH6ico60UshQW3GiEHA7PzTOtXNLSX-3C0'

r = requests.get('https://api.exchangeratesapi.io/latest')

keys = json.loads(r.content)['rates'].keys()
keys = dict(zip(keys, keys))
keys['EUR'] = 'EUR'
keys = dict(sorted(keys.items()))

html = requests.get('https://index.minfin.com.ua/reference/currency/code/').content
tree = lxml.html.document_fromstring(html)
table = tree.find('body/main/div/div/div[1]/div/div[1]/article/table')

for tr in table:
    try:
        if tr[2] is not None and tr[0].text in keys:
                keys[tr[0].text] = tr[2].text.lower()
    except:
        continue