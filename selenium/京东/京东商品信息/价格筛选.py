# coding = utf-8
"""
# @Author : 精彩.
# @Time : 2020/7/24 15:59
# @File : selenium.py
"""
import time
import csv
import json
from lxml import etree
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 输入框回车
from selenium.webdriver import ActionChains


options = webdriver.ChromeOptions()
# 不加载图片
# options.add_experimental_option('prefs', {'profile.managed_default_content_settings.images': 2})
driver = webdriver.Chrome(options=options)
url = 'https://www.jd.com'
driver.get(url)


# 定位到搜索框并输入
input = driver.find_element_by_xpath('//*[@id="key"]')
input.send_keys("平凡的世界")
input.send_keys(Keys.ENTER)
time.sleep(2)

# 最低价
lowValue = driver.find_element_by_xpath('//*[@id="J_selectorPrice"]/div[1]/div[1]/input')
lowValue.send_keys('20')


# 最高价
highValue = driver.find_element_by_xpath('//*[@id="J_selectorPrice"]/div[1]/div[2]/input')
highValue.send_keys('50')
time.sleep(1)


# 保持光标在元素上
ac = driver.find_element_by_xpath('//*[@id="J_selectorPrice"]/div[1]/div[2]/input')
ActionChains(driver).move_to_element(ac).perform()
time.sleep(1)


# 确定
ac1 = driver.find_element_by_xpath('//*[@id="J_selectorPrice"]/div[2]/a[2]')
ac1.click()
time.sleep(2)


# 按销量查找
ac2 = driver.find_element_by_xpath('//*[@id="J_filter"]/div[1]/div[1]/a[2]/span')
ac2.click()
time.sleep(1)


# 返回当前网页url
# htmlUrl = driver.current_url
# print(htmlUrl)
html = driver.page_source.encode('utf-8', 'ignore')
doc = pq(html)
items = doc('#J_goodsList > ul > li').items()
for item in items:
    # lists = {
    #     'name': item('.p-name a').text(),
    #     'price': item('.p-price i').text(),
    #     'commit': item('.p-commit a').text()
    # }
    # print(lists)
    # json_str = json.dumps(lists)
    # with open('E:\python\project\selenium\info.json', 'w')as f:
    #     f.write(json_str + '\n')

    name = item('.p-name a').text()
    price = item('.p-price i').text()
    commit = item('.p-commit a').text()

    with open("E:/python/resource/info.csv", 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name,price,commit])
