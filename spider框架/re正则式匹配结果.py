'''使用 re正则表达式 匹配结果'''
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
        html = r.text
        return html
    except:
        return "error"

def re_(pattern,html):
    lists = re.findall(pattern,html)
    print(lists)

url = "http://www.52myqq.com/Android/qqinfo_61907.html"
pattern = ('\w+@+\w+.com')
txt = getHtml(url)
print(re_(pattern,txt))
