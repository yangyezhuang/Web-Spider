# coding='utf-8'
"""
# @Author : yangyezhuang
# @Time : 2020/7/21 16:33
# @File : spider_comments.py
"""

import requests
import json
import time
import random

headers = {
    "referer": "https://item.jd.com/100004404944.html",
    "user - agent": "Mozilla / 5.0"
}


def spider_comment(page=0):
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchcomment98&productId=100004404944&' \
          'score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1' % page
    try:
        headers = {
            "referer": "https://item.jd.com/100004404944.html",
            "user - agent": "Mozilla / 5.0"
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
    except:
        print("error")
    # 获取json字符串
    json_str = r.text[15:-2]
    # 将json转换为python对象
    json_obj = json.loads(json_str)
    # 获取评价列表
    comments = json_obj['comments']
    # 遍历列表并写入
    for comment in comments:
        with open('E:\python\project\爬京东评论\comments.txt', 'a+') as f:
            f.write(comment['content'])
            f.write('\n')


def change_page():
    for i in range(2):
        spider_comment(i)
        time.sleep(random.random() * 5)
    print("ok")


if __name__ == '__main__':
    # spider_comment()
    change_page()
