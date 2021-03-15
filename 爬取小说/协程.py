import requests
import os
from lxml import etree
import time
import aiohttp
import asyncio
from os.path import dirname, abspath

start = time.time()

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
path = dirname(abspath(__file__)) + '/noval/'
url_list = []


async def get_content(url,semaphore):
    """
    获取文章内容
    """
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, verify_ssl=False,headers=headers) as response:
                if response.status == 200:
                    response = await response.text()
                    html = etree.HTML(response)
                    title_list=[]
                    for tit in html.xpath('//div[@class="box_con"]/div[@class="bookname"]/hi/text()'):
                        title_list.append(tit)
                    text_list=[]
                    for txt in html.xpath('//div[@class="box_con"]/div[@id="content"]/text()'):
                        text_list.append(txt)
                    save(title_list,text_list)


def save(title,txt):
    if not os.path.exists(path):
        os.mkdir(path)
    for i in title:
        for j in txt:
            with open(path + i + '.txt', 'w', encoding='utf-8') as f:
                f.write(j)
    print('下载成功')


async def main():
    semaphore = asyncio.Semaphore(500)
    url = 'http://www.biquku.la/0/421/'
    r = requests.get(url, headers=headers).text
    html = etree.HTML(r)
    class_url = html.xpath('//*[@id="list"]/dl/dd/a/@href')
    for i in class_url:
        url = 'http://www.biquku.la/0/421/' + i
        url_list.append(url)
    tasks = [asyncio.create_task(get_content(url,semaphore)) for url in url_list]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
    end = time.time()
    print(f'用时 {end - start}s')


# //*[@id="content"]/text()[1]
# //*[@id="wrapper"]/div[4]/div/div[2]/h1