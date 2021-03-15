import requests
import re,os
from lxml import etree
from os.path import dirname, abspath

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
url = 'http://www.biquku.la/0/421/'
path = dirname(abspath(__file__)) + '/斗罗大陆/'


def get_info(url):
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    get_info_list = [] # 章节目录列表
    html = etree.HTML(response.text)
    dd_list = html.xpath('//*[@id="list"]/dl/dd')
    for dd in dd_list:
        title = dd.xpath('a/text()')[0]
        href = 'http://www.biquku.la/0/421/' + dd.xpath('a/@href')[0]
        chapter = {'title': title, 'href': href}
        get_info_list.append(chapter)
    return get_info_list


def get_content(get_info):
    for chapter_info in get_info:
        response = requests.get(url=chapter_info['href'], headers=headers)
        response.encoding = 'utf-8'
        if not os.path.exists(path):
            os.mkdir(path)
        contents = re.findall('<div id="content">(.*?)</div>', response.text)
        with open(path + chapter_info['title'] + '.txt', 'w', encoding='utf-8') as f:
            for content in contents:
                f.write(content.replace('&nbsp;&nbsp;&nbsp;&nbsp;', '').replace('<br/><br/>', '\n').strip())
            print(chapter_info['title'])


if __name__ == '__main__':
    get_content(get_info(url))
