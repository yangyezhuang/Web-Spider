import os
import csv
import time
import asyncio
import aiohttp
import requests
from lxml import etree
from os.path import dirname, abspath



start = time.time()

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
path = dirname(abspath(__file__)) + '/公交路线/'
url_list=[]

# 获取内容
async def get_info(url,semaphore):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url,verify_ssl=False,headers=headers) as response:
                if response.status==200:
                    response = await response.text()
                    html = etree.HTML(response)
                    stations = html.xpath('//div[@class="bus-excerpt mb15"]')
                    name = html.xpath('//a[@class="cr_crumbs_txt"][2]/text()')
                    for i in range(0, len(stations)):
                        station = html.xpath('//div[@class="trip"]/text()')[i]
                        line = html.xpath( f'//div[@class="bus-lzlist mb15"]{[i+1]}//li/a/text()')
                        print(station)
                        # print(line)
                        save_csv(name[0], station, line)

# 以csv保存
def save_csv(name, station, line):
    if not os.path.exists(path):
        os.mkdir(path)
    with open(path + '北京全部.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, station, line])


async def main():
    semaphore = asyncio.Semaphore(500)
    url = 'https://beijing.8684.cn'
    html = requests.get(url, headers=headers).text
    html = etree.HTML(html)
    result = html.xpath('//div[@class="pl10"][3]/div[@class="list"]/a/@href')
    for i in result:
        mode_url = 'https://beijing.8684.cn' + i
        html = requests.get(mode_url, headers=headers).text
        html = etree.HTML(html)
        urls = html.xpath('//div[@class="list clearfix"]/a/@href')
        for j in urls:
            url = 'https://beijing.8684.cn'+j
            url_list.append(url)
    tasks = [asyncio.create_task(get_info(url,semaphore)) for url in url_list]
    await asyncio.wait(tasks)


if __name__ == "__main__":
    asyncio.run(main())
    end = time.time()
    print(f'用时 {end - start}s')