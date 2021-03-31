import requests
import json
import csv

f = open('AppData.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['名称', '单价','系统','结算方式','有无后台', 'QQ','产品要求'])
csv_writer.writeheader()

url = 'https://www.cpajia.com/index.php?m=index&a=search'

for i in range(1,3):
    data={'PageIndex':f'{i}'}
    r= requests.post(url,data=data)
    html = r.json()
    lis = html[1:-1]
    dit={}
    for i in lis:
        dit['名称']=i['title']
        dit['单价'] = i['price']
        dit['系统'] = i['platform']
        dit['结算方式'] = i['balance']
        dit['有无后台'] = i['dataview']
        dit['QQ'] = i['qq']
        csv_writer.writerow(dit)
