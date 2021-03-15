# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Author : YangYeZhuang
# @Time : 2020/8/4 11:44
# @File : boss_1.py
"""
import json
import time
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains  # 鼠标动作链

# 不加载图片
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'profile.managed_default_content_settings.images': 2})
browser = webdriver.Chrome(options=options)
wait = WebDriverWait(browser, 15)
url = 'https://www.zhipin.com/'
data_list = []
max_page = 3


def find_work():
    """
    筛选条件
    :return:
    """
    search = browser.find_element_by_class_name('ipt-search')
    search.send_keys('python')
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    jingyan = browser.find_element_by_xpath('//*[@id="filter-box"]/div/div[4]/div[1]/span/input')
    jingyan_1 = browser.find_element_by_xpath('//*[@id="filter-box"]/div/div[4]/div[1]/span/div/ul/li[3]/a')
    ActionChains(browser).move_to_element(jingyan).click(jingyan_1).perform()
    time.sleep(2)
    xueli = browser.find_element_by_xpath('//*[@id="filter-box"]/div/div[4]/div[2]/span/input')
    xueli_1 = browser.find_element_by_xpath('//*[@id="filter-box"]/div/div[4]/div[2]/span/div/ul/li[5]/a')
    ActionChains(browser).move_to_element(xueli).click(xueli_1).perform()  # 将鼠标移动到某个元素的位置并点击


def get_info():
    """
    采集数据
    :return:
    """
    wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#main > div > div.job-list > ul > li"))
    )  # 等待最后一条加载完成
    time.sleep(2)
    html = browser.page_source
    html = pq(html)
    items = html('#main > div > div.job-list > ul > li').items()
    for item in items:
        info = {
            'company': item('.name a').text(),
            'post': item('.job-name a').text(),
            'salary': item('.red').text(),
            'work': item('.tags span').text(),
            'welfare': item('.info-desc').text(),
            'address': item('.job-area').text()
        }
        data_list.append(info)
    print("岗位数量：", len(data_list))
    save_next()


def save_next():
    """
    保存后翻页
    :return:
    """
    content = json.dumps(data_list, ensure_ascii=False, indent=2)
    with open("E:\python\project\selenium\BOSS直聘\info.json", "w", encoding="utf-8") as f:
        f.write(content)
    time.sleep(2)
    botton = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#main > div > div.job-list > div.page > a.next'))
    )
    botton.click()


def main():
    browser.get(url)
    find_work()
    for i in range(1, max_page + 1):
        print("第", i, "页：")
        get_info()
    #browser.quit()


if __name__ == '__main__':
    main()
