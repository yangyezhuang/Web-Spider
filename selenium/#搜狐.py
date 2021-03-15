import time
from lxml import etree
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.sohu.com/')


def search():
    try:
        # classname为”txt”的页面元素中的文本
        elements = driver.find_elements_by_class_name('txt')
        for i in elements:
            if i.text == '':
                pass
            else:
                print(i.text)

        # 标签为”footer”的页面元素中的文本
        elements = driver.find_elements_by_class_name('footer')
        for i in elements:
            if i.text == '':
                pass
            else:
                print(i.text)

        # 用xpath获取搜狐首页的导航栏标签中的文本
        elements = driver.find_elements_by_xpath('//nav[@class="nav area"]//a')
        for i in elements:
            if i.text == '':
                pass
            else:
                print(i.text)

        # html = driver.page_source
        # # print(html)
        # html = etree.HTML(html)
        # result = html.xpath('//nav[@class="nav area"]//a/text()')
        # for i in result:
        #     print(i)

        driver.quit()
    except TimeoutException:
        return search()


if __name__ == "__main__":
    search()
