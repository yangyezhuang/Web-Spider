import json

# 1.实现python数据结构与json字符串之间的转换
# dictdata = {
#     'no':1,
#     'name':'Tom',
#     'score':80
# }

# jsonstr = json.dumps(dictdata)'''python转json'''
# print(jsonstr)

# adict = json.loads(jsonstr)'''json转python'''
# print(adict)


# 2.读取json文件，获取内容
adict = {}
with open('E:\python\文件\info.json', 'r', encoding='utf-8') as f:
    adict = json.load(fp=f)
    print(adict)
    for key, value in adict.items():
        print(key)
        print(value)
'''更新json数据'''
b = dict(web=[{'no': '4', 'name': '百度', 'url': 'www.baidu.com'}])
adict.update(b)
print(adict)

'''将json数据写入新文件'''
with open('E:\python\文件\info1.json', 'w', encoding='utf-8') as f:
    json.dump(adict, fp=f)



# 3.实例
import requests
import json

def getHtml(url):
    try:
        headers = {
            "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        session = requests.session
        if not url:
            raise ("必须提供url")
        if queryload:
            if not isinstance(queryload, dict):
                raise ("get方法的查询参数格式必须是字典：", queryload)

        r = session.get(url, params=queryload, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except requests.exceptions as e:
        print(e)
        return "error"


if __name__ == "__main__":

rl = 'http://vip.stock.finance.sina.com.cn/mkt/#stock_sz_up'
r = getHtml(url)
print(r)

# 将获取到的数据存为json文件
with open('E:\python\文件\info2.json', 'w', encoding='utf-8') as f:
    json.dump(r, fp=f, ensure_ascii=False)