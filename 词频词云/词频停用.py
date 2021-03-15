# coding=gbk
"""
# @Author : yangyezhuang
# @Time : 2020/7/23 10:50
# @File : cp.py
"""
import jieba
import wordcloud


# def stop_list(stop_path):
#     stopWordList = []
#     with open(stop_path) as f:
#         for i in f.readlines():
#             lst = i.strip().split(".")
#             stopWordList.append(i)
#     return stopWordList


# 对文本进行分词
def cut_word(file_path):
    file = open(file_path, 'r')
    txt = file.read()
    words = jieba.lcut(txt)
    # 对词频进行统计
    count = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            count[word] = count.get(word, 0) + 1
    return count


def stopWord(count):
    exclude = ["手机", "其他", "非常", "使用", "一天"]  # 建立无关词语列表
    for key in list(count.keys()):  # 遍历字典的所有键，即所有word
        if key in exclude:
            del count[key]
    lists = list(count.items())
    lists.sort(key=lambda x: x[1], reverse=True)
    # 打印前15条词频
    for i in range(20):
        word, number = lists[i]
        print("关键字：{:-<5}频次：{}".format(word, number))

# 词频写入
def writeTxt(count):
    with open(word_path, 'w', encoding='gbk') as f:
        for i in range(20):
            word, number = lists[i]
            f.write('{}\t{}\n'.format(word, number))
        f.close()
        return word_path


# 制作词云
def get_cloud(word_path):
    with open(word_path, 'r', encoding='gbk') as f:
        text = f.read()
    wcloud = wordcloud.WordCloud(font_path=r'C:\Windows\Fonts\simhei.ttf',
                                 background_color='white',
                                 width=500,
                                 max_words=1000,
                                 height=400,
                                 margin=2).generate(text)
    wcloud.to_file('E:\python\project\词频词云/' + 'cloud2.png')  # 指定词云文件路径
    f.close()
    print("词云图片已保存")


file_path = 'E:\python\project\爬京东评论\comments.txt'
word_path = 'E:\python\project\词频词云\wordcloud.txt'
# stop_path = 'E:\python/resource\停用词.txt'

if __name__ == '__main__':
    cut_word(file_path)
    stopWord(count)
    writeTxt(count)
    get_cloud(word_path)
