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
wait = WebDriverWait(browser, 10)  # 设置等待时间
base_url = 'https://search.jd.com/Search?keyword='
DATA = []  # 设置全局变量用来存储数据
KEYWORD = '书'  # 商品名称
MAX_PAGE = 50


def index_page(page):
    """翻页函数，
    Args:
        page (int): 页码
    """
    print('正在爬取第{}页'.format(page))
    try:
        if page > 1:

            input_skip = wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > input'
            )))
            button_submit = wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, '#J_bottomPage > span.p-skip >a'
            )))
            input_skip.clear()
            input_skip.send_keys(page)
            browser.execute_script("arguments[0].click();", button_submit)

        browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        # 等待60个商品加载完毕
        wait.until(EC.presence_of_all_elements_located((
            By.CSS_SELECTOR, "#J_goodsList > ul > li:nth-child(60)"
        )))

        # 确认翻页完毕
        wait.until(EC.text_to_be_present_in_element((
            By.CSS_SELECTOR, "#J_bottomPage > span.p-num > a.curr"), str(page)
        ))
        html = browser.page_source
        find_save(html, page)
    except TimeoutException:
        print('Error')
        index_page(page)


def find_save(html, page):
    """筛选商品信息
    Args:
        html (str): 网页源码
    """
    doc = pq(html)
    items = doc('#J_goodsList > ul > li').items()
    count = 0
    for item in items:
        count += 1
        product = {
            'name': item('.p-name a').text(),
            'price': item('.p-price i').text(),
            'commit': item('.p-commit a').text()
        }
        DATA.append(product)  # 写入全局变量
    # 记录已爬取的商品个数，便于调试
    if count == 60:
        print('Success!')
    else:
        print('Error!')
        index_page(page)


def save_to_jason():
    """以json的形式保存
    """
    with open('info.json', 'w', encoding='utf-8')as file:
        file.write(json.dumps(DATA, indent=2, ensure_ascii=False))


def main():
    # 完整的url
    url = base_url + quote(KEYWORD)
    browser.get(url=url)
    for i in range(1, MAX_PAGE+1):
        index_page(i)
    save_to_jason()


if __name__ == "__main__":
    main()