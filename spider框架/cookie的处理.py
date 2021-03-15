# 使用会话对象处理cookie
import requests


def getHtml(url,cookies):
    try:
        headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        s = requests.Session()
        s.cookies.update(cookies)
        r = s.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "error"

url = "http://i.baidu.com/"
cookies = dict(BIDUPSID='41AFE94758CE8CA073AB8054AB333C5A',
                PSTM='1582627180',
                BAIDUID='41AFE94758CE8CA00EB02602B1356AE4:FG=1',
                BDUSS='jBrSWxQZkNMcHYwRjluQnpmbGlCZnVVaTBuTGNIdnpHZXhWT0gtTFNPOXlUSkplRVFBQUFBJCQAAAAAAAAAAAEAAACnXH2RWVlazfjC59fK1LTVvgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHK~al5yv2peY',
                H_PS_PSSID='1448_31672_32139_31660_32045_32230_32259_26350',
                PHPSESSID='k8fgbje84v6cdlo6rof9cctj66',
                Hm_lvt_4010fd5075fcfe46a16ec4cb65e02f04='1594453978',
                Hm_lpvt_4010fd5075fcfe46a16ec4cb65e02f04='1594454011')
print(getHtml(url,cookies))
