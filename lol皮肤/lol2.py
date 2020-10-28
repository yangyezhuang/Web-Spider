# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Author : YangYeZhuang
# @Time : 2020/7/31 10:00
# @File : lol3.py
"""

import json
import requests
import os
from time import perf_counter

# 开始计时
start = perf_counter()
headers = {
    'user - agent':
        'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 84.0.4147.89Safari / 537.36'
}
hero_url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
base_url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/'
file_path = 'E:\python\Spider\lol皮肤\image'


def get_info(base_url):
    """
    获取英雄名并创建文件夹
    :param base_url:    :return:
    """
    url = base_url + str(i) + '.js'
    r = requests.get(url)
    info = r.json()
    hero = info.get('hero').get('name')
    skins = info.get('skins')
    path = file_path + '/' + hero
    if not os.path.exists(path):
        os.mkdir(path)
    get_skin(path, skins)
    print(hero + ' —— ok')


def get_skin(path, skins):
    """
    获取皮肤并保存
    :param path:
    :param skins:
    :return:
    """
    for skin in skins:
        skin_name = skin.get('name')
        skin_url = skin.get('mainImg')
        if skin_url == '':
            continue
        img = requests.get(skin_url, headers=headers)
        if not os.path.exists(path + '/' + skin_name + '.jpg'):
            with open(path + '/' + skin_name + '.jpg', 'wb')as f:
                f.write(img.content)


if __name__ == '__main__':
    r = requests.get(hero_url)
    hero_json = r.json()
    hero_json = hero_json['hero'] # 获取英雄数量
    for i in range(1, len(hero_json)):
        get_info(base_url)
    print('用时{:.3f}s'.format(start - perf_counter()))
