import re

import requests
from lxml import html

url = 'https://www.ip-adress.com/proxy-list'
request = requests.get(url)

tree = html.document_fromstring(request.text)

ip = tree.xpath('/html/body/main/table/tbody/tr/td/a/text()')

ports = tree.xpath('/html/body/main/table/tbody/tr/td/text()')

port = [re.findall(r'\S\d{2,4}', i) for i in ports if re.findall(r'\S\d{2,4}', i)]

res = [(ip[i] + str(port[i]).replace("'", "").replace("[", "").replace("]", "")) for i in range(len(ip))]
for i in res:
    print(i)
