import requests
from lxml import etree

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
city_url_list = []
url = 'https://www.lianjia.com/city/'
r = requests.get(url, headers=headers)
html = r.text
html = etree.HTML(html)
result = html.xpath('//ul[@class="city_list_ul"]/li//div[@class="city_province"]/ul/li/a/@href')
for li in result:
    for i in range(1, 3):
        url = li + f'ershoufang/pg{i}'
        city_url_list.append(url)
print(len(city_url_list))
print(city_url_list)
