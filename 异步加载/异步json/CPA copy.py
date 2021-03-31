import requests
import json
import csv

def get_html(url):
    data={'PageIndex':f'{i}'}
    r= requests.post(url,data=data)
    html = r.json()
    get_json(html)


def get_json(html):
    lis = html[1:-1]
    dit={}
    for i in lis:
        dit['名称']=i['title']
        dit['单价'] = i['price']
        dit['系统'] = i['platform']
        dit['结算方式'] = i['balance']
        dit['有无后台'] = i['dataview']
        dit['QQ'] = i['qq']
        dit['产品要求'] = i['content'][1:11]
        save_csv(dit)

def save_csv(dit):
    with open('AppData.csv', mode='a', encoding='utf-8', newline='')as f:
        writer = csv.DictWriter(f, fieldnames=['名称', '单价','系统','结算方式','有无后台', 'QQ','产品要求'])
        writer.writeheader()
        writer.writerow(dit)


if __name__ =='__main__':
    for i in range(1,3):
        url = 'https://www.cpajia.com/index.php?m=index&a=search'
        get_html(url)

        
