# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Author : YangYeZhuang
# @Time : 2020/7/29 10:50
# @File : taobao.py
"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 20)  # 设置等待时间


def logon():
    browser.get('https://www.taobao.com/')
    try:
        button = wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                '#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-sign > a.h'
            )))
        button.click()  # 点击登录按钮
        # 找到输入框
        username = browser.find_element_by_id('fm-login-id')
        password = browser.find_element_by_id('fm-login-password')
        time.sleep(1)
        username.send_keys('18403426152')
        password.send_keys('yang1127520')
        time.sleep(1)
        # 找到滑块
        ac = browser.find_element_by_id('nc_1__bg')
        # 点击并保持
        ActionChains(browser).click_and_hold(ac).perform()
        # 拖动滑块
        ActionChains(browser).move_by_offset(xoffset=300, yoffset=0).perform()
        # 等待验证
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR,
                 'div#nc_1__scale_text > span.nc-lang-cnt > b'), '验证通过'))
        # 点击登录
        browser.find_element_by_xpath(
            '//*[@id="login-form"]/div[4]/button').click()
        print("登陆成功")
    except TimeoutException as e:
        print('Error:', e.args)
        logon()


if __name__ == "__main__":
    logon()
