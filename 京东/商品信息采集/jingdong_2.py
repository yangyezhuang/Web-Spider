# -*- coding: utf-8 -*-
"""
# @Author : YangYeZhuang
# @Time : 2020/7/27 15:31
# @File : jingdong2.py
"""

import time
import json
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import quote
from selenium.common.exceptions import TimeoutException

# 不加载图片
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'profile.managed_default_content_settings.images': 2})
browser = webdriver.Chrome(options=options)
base_url = 'https://search.jd.com/Search?keyword='
wait = WebDriverWait(browser, 20)  # 设置等待时间
data_list = []  # 设置全局变量用来存储数据
keyword = "剃须刀"  # 商品名称
max_page = 5


def change_page():
    try:
        wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#J_goodsList > ul > li:nth-child(30)"))
        )  # 等到30个商品都加载出来
        time.sleep(2)
        # 下拉
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#J_goodsList > ul > li:nth-child(60)"))
        )  # 等待最后一个商品信息加载完毕
        html = browser.page_source
        find_save(html)  # 调用函数筛选数据
        button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.pn-next > em'))
        )  # 等待翻页按钮可以点击
        button.click()  # 点击翻页按钮
    except TimeoutException:
        print("Error")
        change_page()


def find_save(html):
    """
    筛选数据以json形式保存
    :param html:
    :return:
    """
    doc = pq(html)
    items = doc('#J_goodsList > ul > li').items()
    for item in items:
        product = {
            'name': item('.p-name a').text(),
            'price': item('.p-price i').text(),
            'commit': item('.p-commit a').text()
        }
        data_list.append(product)  # 写入全局变量
    print('商品个数：', len(data_list))
    # 把全局变量转化为json数据
    content = json.dumps(data_list, ensure_ascii=False, indent=2)
    with open("E:\python\project\selenium\京东商品\info.json", "w", encoding="utf-8") as f:
        f.write(content)


def main():
    url = base_url + quote(keyword)
    browser.get(url)
    for i in range(1, max_page + 1):
        print("第", i, "页：")
        change_page()
    browser.quit()


if __name__ == "__main__":
    main()
