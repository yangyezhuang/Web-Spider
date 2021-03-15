import requests
import re

url = "http://www.52myqq.com/Android/qqinfo_61907.html"

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}
r = requests.get(url, headers=headers)
r.raise_for_status()
r.encoding = r.apparent_encoding
html = r.text

account = re.findall('\\w+@+\\w+.com', html)
passwd = re.findall('----(.*?)\n', html)
print('邮箱：', account)
print('\n')
print('密码：', passwd)


# for i in account:
#     print(i)
