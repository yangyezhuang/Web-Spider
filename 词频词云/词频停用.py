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


# ���ı����зִ�
def cut_word(file_path):
    file = open(file_path, 'r')
    txt = file.read()
    words = jieba.lcut(txt)
    # �Դ�Ƶ����ͳ��
    count = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            count[word] = count.get(word, 0) + 1
    return count


def stopWord(count):
    exclude = ["�ֻ�", "����", "�ǳ�", "ʹ��", "һ��"]  # �����޹ش����б�
    for key in list(count.keys()):  # �����ֵ�����м���������word
        if key in exclude:
            del count[key]
    lists = list(count.items())
    lists.sort(key=lambda x: x[1], reverse=True)
    # ��ӡǰ15����Ƶ
    for i in range(20):
        word, number = lists[i]
        print("�ؼ��֣�{:-<5}Ƶ�Σ�{}".format(word, number))

# ��Ƶд��
def writeTxt(count):
    with open(word_path, 'w', encoding='gbk') as f:
        for i in range(20):
            word, number = lists[i]
            f.write('{}\t{}\n'.format(word, number))
        f.close()
        return word_path


# ��������
def get_cloud(word_path):
    with open(word_path, 'r', encoding='gbk') as f:
        text = f.read()
    wcloud = wordcloud.WordCloud(font_path=r'C:\Windows\Fonts\simhei.ttf',
                                 background_color='white',
                                 width=500,
                                 max_words=1000,
                                 height=400,
                                 margin=2).generate(text)
    wcloud.to_file('E:\python\project\��Ƶ����/' + 'cloud2.png')  # ָ�������ļ�·��
    f.close()
    print("����ͼƬ�ѱ���")


file_path = 'E:\python\project\����������\comments.txt'
word_path = 'E:\python\project\��Ƶ����\wordcloud.txt'
# stop_path = 'E:\python/resource\ͣ�ô�.txt'

if __name__ == '__main__':
    cut_word(file_path)
    stopWord(count)
    writeTxt(count)
    get_cloud(word_path)
