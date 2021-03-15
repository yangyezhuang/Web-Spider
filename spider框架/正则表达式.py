import requests
import re


def getHtml(url):
    try:
        headers = {
            "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "error"


url = "http://www.52myqq.com/Android/qqinfo_61907.html"
rule = ('\w+@+\w+.com')

html = getHtml(url)
lists = re.findall(rule, html)
with open('E:\python\project\正则式测试\邮箱.txt', 'w') as f:
    for i in lists:
        f.write(i + '\n')

# (u'[\u4e00-\u9fa5]+') # 匹配中文
