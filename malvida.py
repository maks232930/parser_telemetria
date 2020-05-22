import random
import requests
from bs4 import BeautifulSoup



def get_proxy():
    request = requests.get('https://xseo.in/freeproxy')
    soup = BeautifulSoup(request.content, 'html.parser')
    result = soup.find_all('tr', attrs={'class': 'cls81'})
    proxy_list = [div.find('font', attrs={'class': 'cls1'}).text for div in result]

    for proxy in random.choice(proxy_list):
        try:
            url = "http://" + proxy
            r = requests.get('https://yandex.by', proxies={'http': url})
            if r.status_code == 200:
                return url
        except requests.exceptions.ConnectionError:
            continue


def main():
    url = 'https://malvina-club.ru/hours/'
    request = requests.get(url, proxies={'http': get_proxy()})
    soup = BeautifulSoup(request.content, 'lxml')
    hours = soup.find_all('tr', attrs={'class': 'hours'})
    print(hours)


if __name__ == '__main__':
    main()
