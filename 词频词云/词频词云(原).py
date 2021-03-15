# coding = utf-8
"""
# @Author : yangyezhuang
# @Time : 2020/7/22 18:25
# @File : wc.py
"""
import jieba
import wordcloud

# 对文本进行分词
file = open('E:\python\project\爬京东评论\comments.txt', 'r')
txt = file.read()
words = jieba.lcut(txt)

# 对词频进行统计
count = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        count[word] = count.get(word, 0) + 1

lists = list(count.items())
lists.sort(key=lambda x: x[1], reverse=True)

# 将词频写入文件
for i in range(10):
    word, number = lists[i]
    print("关键字：{:-<5}频次：{}".format(word, number))
    with open('E:\python\project\词频词云\wordcloud.txt', 'w', encoding='utf-8') as f:
        for i in range(10):
            word, number = lists[i]
            f.write('{}\t{}\n'.format(word, number))

# 制作词云
with open('E:\python\project\词频词云\wordcloud.txt', 'r', encoding='utf-8') as f:
    text = f.read()
wcloud = wordcloud.WordCloud(font_path=r'C:\Windows\Fonts\simhei.ttf',
                             background_color='white',
                             width=1000,
                             max_words=1000,
                             height=860).generate(text)
wcloud.to_file('E:\python\project\词频词云/' + 'cloud.png')  # 指定词云文件路径
print("词云图片已保存")
