# -*- coding: utf-8 -*-
"""
# @Author : yangyezhuang
# @Time : 2020/7/16 11:46
# @File : 使用selenium设置鼠标动作链.py
"""

# 鼠标移动到某个元素位置
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

ac = driver.find_element_by_xpath('//div/a[@href="http://news.baidu.com"]')

'''驱动driver移动到元素上'''
# ActionChains(driver).move_to_element(ac).perform()
ActionChains(driver).move_to_element(ac).click(ac).perform()  # 将鼠标移动到某个元素的位置并点击
# ActionChains(driver).move_to_element(ac).double_click(ac).perform()  # 将鼠标移动到某个元素的位置并双击
# ActionChains(driver).move_to_element(ac).context_click(ac).perform()  # 将鼠标移动到某个元素的位置并右击
# ActionChains(driver).move_to_element(ac).click_and_hold(ac).perform()  # 在某个元素的位置左键单击hold住
# ActionChains(driver).drag_and_drop(ac, ac1).perform()  # 将某个元素拖拽到另一个元素

time.sleep(2)
