import requests
import re

URL = 'https://store.data-analyst.praktikum-services.ru/'
req_text = requests.get(URL).text
found_products = re.findall('Молоко [A-z + А-я + -]+', req_text)
print(len(found_products))
print(found_products)
