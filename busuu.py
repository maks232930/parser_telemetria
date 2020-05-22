from bs4 import BeautifulSoup
import requests

session = requests.Session()
url = 'https://www.kufar.by/login/'
data = {
    'email': '',
    'password': ''
}

request = requests.post(url, data=data)
with open('result.txt', '+a') as f:
    f.write(request.text)
