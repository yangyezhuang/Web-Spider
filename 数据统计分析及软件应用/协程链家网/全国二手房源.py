import os
import csv
import asyncio
import aiohttp
import requests
from lxml import etree
from os.path import dirname, abspath

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
path = dirname(abspath(__file__)) + '/data/'


# 解析数据
async def parse(url):
    async with aiohttp.ClientSession()as session:
        async with session.get(url, verify_ssl=False, headers=headers)as response:
            if response.status == 200:
                response = await response.text()
                html = etree.HTML(response)
                lists = html.xpath('//ul[@class="sellListContent"]/li')
                for li in lists:
                    city = html.xpath('//h2[@class="total fl"]/text()[2]')[0][1:-3]
                    community = li.xpath('./div[1]/div[2]//a/text()')[0].strip()
                    location = li.xpath('./div[1]/div[2]//a/text()')[1]
                    total_price = li.xpath('./div[1]/div[6]/div[1]/span/text()')[0] + '万'
                    unit_price = li.xpath('./div[1]/div[6]/div[2]/span/text()')[0].strip('单价')
                    layout = li.xpath('./div[1]/div[3]/div/text()')[0].split('|')[0].strip()
                    area = li.xpath('./div[1]/div[3]/div/text()')[0].split('|')[1].strip()
                    floor = li.xpath('./div[1]/div[3]/div/text()')[0].split('|')[-2].strip()
                    house_type = li.xpath('./div[1]/div[3]/div/text()')[0].split('|')[-3].strip()

                    save(city, community, location, total_price, unit_price, layout, area, floor, house_type)


# 保存为csv
def save(city, community, location, total_price, unit_price, layout, area, floor, house_type):
    if not os.path.exists(path):
        os.mkdir(path)
    with open(path + '全国二手房2.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([city, community, location, total_price, unit_price, layout, area, floor, house_type])


# 构造任务列表
async def main():
    url_list = []
    url = 'https://www.lianjia.com/city/'
    r = requests.get(url, headers=headers)
    html = r.text
    html = etree.HTML(html)
    result = html.xpath('//ul[@class="city_list_ul"]/li//div[@class="city_province"]/ul/li/a/@href')
    for li in result:
        for i in range(1, 101):
            url = li + f'ershoufang/pg{i}'
            url_list.append(url)
    tasks = [asyncio.create_task(parse(url)) for url in url_list]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
