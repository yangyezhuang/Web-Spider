#encoding='utf-8'
import requests
from lxml import etree


def getHtml(url):
    try:
        headers = {
            "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = 'gbk'
        return r.text
    except:
        return "error"


url = 'https://gp.qq.com/cp/a20190522gamedata/pc_list.shtml'
doc = etree.HTML(getHtml(url))
result = doc.xpath('//ul[@class="imgtextlist"]//a/p/text()')
for i in result:
    print(i)
