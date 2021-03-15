# 使用BeautifulSoup库解析类xml文档
import requests
from bs4 import BeautifulSoup


def getHtml(url):
    try:
        headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
        return html
    except:
        return "error"


url = "http://www.52myqq.com/Android/qqinfo_61907.html"
txt = getHtml(url)
# 1.利用tag对象属性，获取tag内容
bsobj = BeautifulSoup(txt)
# print(bsobj.li.a)

# 2.查找所有的li元素，并返回内容
lists = bsobj.find_all(name=bsobj.li.name)
for i in lists:
    print(i)

# 3.查找标题为“···”的超链接
result = bsobj.findAll(name="div")
for i in result:
    if i.a and i.a.string == "qq号码估价吉凶测试 你的qq号怎么样?":
        print(i.a)
        if i.a:
            print(i.a.attrs['href'])
