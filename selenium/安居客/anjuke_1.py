# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Author : YangYeZhuang
# @Time : 2020/7/31 20:22
# @File : lianjia1.py
"""

import json
import time
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

url = 'https://tianjin.anjuke.com/sale/'
info_list = []
max_page = 1

# 无图模式
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'profile.managed_default_content_settings.images': 2})
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)  # 设置等待时间


def find():
    wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#houselist-mod-new > li:nth-child(60)"))
    )  # 等待最后一个商品信息加载完毕
    time.sleep(2)
    html = driver.page_source
    save(html)
    button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#content > div.sale-left > div.multi-page > a.aNxt"))
    )
    button.click()


def save(html):
    html = pq(html)
    items = html('#houselist-mod-new > li').items()
    for item in items:
        info = {
            'name': item('.house-title a').text(),
            'price': item('.price-det strong').text(),
            'avg_price': item('.unit-price').text(),
            'address': item('.details-item span').text()
        }
        info_list.append(info)
        content = json.dumps(info_list, ensure_ascii=False, indent=2)
        with open('/home/yyz/Code/python/Spider/selenium/安居客/info.json', 'w', encoding="utf-8")as f:
            f.write(content)


def main():
    driver.get(url)
    for i in range(1, max_page + 1):
        print("第", i, "页：")
        find()
    driver.quit()


if __name__ == '__main__':
    main()
