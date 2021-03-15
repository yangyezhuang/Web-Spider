import os
import re
import time
import json
import requests
from lxml import etree
from hashlib import md5
from urllib.parse import urlencode
from multiprocessing.pool import Pool


headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 Edg/81.0.416.68',
}


# 获取网页内容
def get_page(offset):
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '美女',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
        'timestamp': f'{int(time.time())}'
    }
    # 用 urlencode() 方法构造请求的 GET 参数
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)
    try:
        r = requests.get(url=url, params=params, headers=headers)
        if r.status_code == 200:
            html = r.json()
            get_info(html)
    except requests.ConnectionError:
        return None


# 解析列表url
def get_info(json):
    if json.get('data'):
        for item in json.get('data'):
            if item.get('title') is None:
                continue
            title = item.get('title')
            if item.get('article_url') is None:
                continue
            urls = item.get('article_url')
            print(title)
            print(urls)
            save(title, urls)


# 创建目录并保存
def save(title, url):
    path = os.path.dirname(__file__) + f'/{title}/'
    if not os.path.exists(path):
        os.mkdir(path)
    html = requests.get(url, headers=headers).text
    html = etree.HTML(html)
    img_urls = html.xpath('//div[@class="pgc-img"]/img/@src')
    for url in img_urls:
        img_name = str(url.split('/')[-1])[:-8] + '.jpg'
        img = requests.get(url, headers=headers)
        with open(path + img_name, 'wb') as f:
            f.write(img.content)


def main():
    for offset in range(0, 20, 20):
        get_page(offset)


if __name__ == "__main__":
    main()