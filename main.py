from time import sleep

import requests
from bs4 import BeautifulSoup as bs

url = 'https://telemetr.me/channels'

with requests.Session() as se:
    se.headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    resp = se.get(url)

index = bs(resp.content, 'html.parser')

max_page = int(input("Введите предполагаемое количество страниц: "))
pages = []
input_category = str(input("Введите категорию. С правильным регистром: "))

for x in range(1, max_page + 1):
    sleep(3)
    pages.append(se.get(f'https://telemetr.me/channels/cat/{input_category}/?page=' + str(max_page)))

for sort in pages:
    pars = bs(sort.content, 'html.parser')

    for el in pars.select('.wd-300'):
        link = el.find('a')

        try:
            print(link.get('href'))
            with open(f'{input_category}.txt', '+a') as file:
                file.write(f'{link.get("href")}\n')

        except AttributeError as error:
            print(f'Произошла ошибка {error}. Работа скрипта продалжается')
            continue
