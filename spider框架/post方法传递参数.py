# 使用post方法传递参数
import requests

def getHtmlByPost(url, querystr):
    try:
        headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        queryload = {'wd': querystr}
        r = requests.post(url, data=queryload, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "error"


url = "https://s.taobao.com/list?spm="
formdata = {'':''}
print(getHtmlByPost(url, '北京'))