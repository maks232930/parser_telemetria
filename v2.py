import requests
from bs4 import BeautifulSoup


def get_proxy():
    proxy_url = 'https://xseo.in/freeproxy'
    request = requests.get(proxy_url)
    soup = BeautifulSoup(request.content, 'html.parser')
    result = soup.find_all('tr', attrs={'class': 'cls81'})
    proxy_list = [div.find('font', attrs={'class': 'cls1'}).text for div in result]

    for proxy in proxy_list[3:]:
        try:
            url = "http://" + proxy
            r = requests.get('https://yandex.by', proxies={'http': url})
            if r.status_code == 200:
                return url
        except requests.exceptions.ConnectionError:
            continue


def telemetria_pars(category):
    try:
        url = f'https://telemetr.me/channels/cat/{category}/?page=1'
        proxy = get_proxy()
        pg = requests.get(url, proxies={'http': proxy})
        soup = BeautifulSoup(pg.content, 'html.parser')
        max_pagination = soup.find_all('div', attrs={'class': 'col-7 col-md-3'})
        max_pages = int(max_pagination[-1].text)

        pagination = [
            requests.get(f'https://telemetr.me/channels/cat/{category}/?page=' + str(i), proxies={'http': proxy})
            for i in range(1, max_pages + 1)
        ]

        for page in pagination:
            bs = BeautifulSoup(page.content, 'html.parser')
            divs = bs.find_all('td', attrs={'class': 'wd-300 pb-0 overflow-hidden'})

            for div in divs:
                title = div.find('a', attrs={'class': 'kt-ch-title'}).text
                href = div.find('a', attrs={'class': 'kt-ch-title'})['href']

                with open(f'{category}.txt', '+a', encoding='utf-8') as f:
                    f.write(f'{title} \n {href} \n\n')

    except IndexError as error:
        print(f'Такой категории нет! {error} или вас временно заблокировал сайт')


category = str(input("Введите категорию с правильным регистром: "))
telemetria_pars(category)
