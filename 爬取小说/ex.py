from os import write
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
html = requests.get('http://www.biquku.la/0/421/224032.html',headers=headers).text
html = etree.HTML(html)
result = html.xpath('//div[@class="bookname"]/h1/text()')
# for i in result:
with  open('E:\python\Spider\爬取小说\dldl.txt','a',encoding='utf-8') as f:
        f.write(result)