import requests


'''requests基本框架'''
# def getHtml(url):
#     try:
#         headers = {
#             "User-Agent":
#             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
#         }
#         r = requests.get(url, headers=headers)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return "error"

# url = "http://i.baidu.com"
# print(getHtml(url))


'''使用get方法提交参数'''
# def getHtmlByGet(url, querystr):
#     try:
#         headers = {
#             "User-Agent":
#             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
#         }
#         queryload = {'wd': querystr}
#         r = requests.get(url, params=queryload, headers=headers)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return "error"


# url = "https://www.baidu.com/s?"
# print(getHtmlByGet(url, '北京'))


'''使用post方法传递参数'''
# def getHtmlByPost(url, querystr):
#     try:
#         headers = {
#             "User-Agent":
#             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
#         }
#         queryload = {'wd': querystr}
#         r = requests.post(url, data=queryload, headers=headers)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return "error"


# url = "https://s.taobao.com/list?spm="
# formdata = {'':}
# print(getHtml(url, '北京'))


'''使用会话对象处理cookie'''
# def getHtml(url,cookies):
#     try:
#         headers = {
#             "User-Agent":
#             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
#         }
#         s = requests.Session()
#         s.cookies.update(cookies)
#         r = s.get(url, headers=headers)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return "error"

# url = "http://i.baidu.com/"
# cookies = dict(BIDUPSID='41AFE94758CE8CA073AB8054AB333C5A',
#                 PSTM='1582627180',
#                 BAIDUID='41AFE94758CE8CA00EB02602B1356AE4:FG=1',
#                 BDUSS='jBrSWxQZkNMcHYwRjluQnpmbGlCZnVVaTBuTGNIdnpHZXhWT0gtTFNPOXlUSkplRVFBQUFBJCQAAAAAAAAAAAEAAACnXH2RWVlazfjC59fK1LTVvgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHK~al5yv2peY',
#                 H_PS_PSSID='1448_31672_32139_31660_32045_32230_32259_26350',
#                 PHPSESSID='k8fgbje84v6cdlo6rof9cctj66',
#                 Hm_lvt_4010fd5075fcfe46a16ec4cb65e02f04='1594453978',
#                 Hm_lpvt_4010fd5075fcfe46a16ec4cb65e02f04='1594454011')
# print(getHtml(url,cookies))


'''使用 re正则表达式 匹配结果'''
# import re
# def getHtml(url):
#     try:
#         headers = {
#             "User-Agent":
#             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
#         }
#         r = requests.get(url, headers=headers)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         html = r.text
#         return html
#     except:
#         return "error"

# def re_(pattern,html):
#     lists = re.findall(pattern,html)
#     print(lists)

# url = "http://www.52myqq.com/Android/qqinfo_61907.html"
# pattern = ('\w+@+\w+.com')
# txt = getHtml(url)
# print(re_(pattern,txt))




'''使用BeautifulSoup库解析类xml文档'''
# import requests
# from bs4 import BeautifulSoup

# def getHtml(url):
#     try:
#         headers = {
#             "User-Agent":
#             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
#         }
#         r = requests.get(url, headers=headers)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         html = r.text
#         return html
#     except:
#         return "error"


# url = "http://www.52myqq.com/Android/qqinfo_61907.html"
# txt = getHtml(url)
# # 1.利用tag对象属性，获取tag内容
# bsobj = BeautifulSoup(txt)
# # print(bsobj.li.a)

# # 2.查找所有的li元素，并返回内容
# lists = bsobj.find_all(name=bsobj.li.name)
# for i in lists:
#     print(i)

# # 3.查找标题为“···”的超链接
result = bsobj.findAll(name="div")
for i in result:
    if i.a and i.a.string == "qq号码估价吉凶测试 你的qq号怎么样?":
        print(i.a)
        if i.a:
            print(i.a.attrs['href'])

