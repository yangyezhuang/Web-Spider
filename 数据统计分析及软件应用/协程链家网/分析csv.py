import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pymysql

df = pd.read_csv(r'E:\Code\PycharmProjects\数据统计分析及软件应用\协程链家网\data\一线城市.csv')


# print("数据行数:", len(df))
# print(list(data.index))  # 获取行索引
# print(data['total_price'].tolist())  # 将df列转化为列表

class House(object):
    def __init__(self):
        self.font = {
            'color': 'r',
            'size': 13
        }

    plt.figure(figsize=(30, 20))
    plt.subplots_adjust(wspace=0.7, hspace=0.5)
    plt.rcParams['font.family'] = 'simhei'
    plt.rcParams['axes.unicode_minus'] = False

    # 各城市二手房平均价格
    def total_price_mean(self):
        data = df.groupby(['city']).mean().round(2)
        city = list(data.index)  # 获取行索引
        total_price_mean = data['total_price'].tolist()  # 将df列转化为列表
        plt.subplot(231)
        plt.title('各城市二手房平均价格', fontdict=self.font)
        plt.bar(city, total_price_mean, label='万元')
        for x, y in enumerate(total_price_mean):
            plt.text(x, y, y, ha='center')
        plt.legend()

    # 各城市二手房/平米平均价格
    def unit_price_mean(self):
        data = df.groupby(['city']).mean().round(2)
        city = list(data.index)
        unit_price_mean = data['unit_price'].tolist()
        plt.subplot(232)
        plt.title('各城市二手房/平米平均价格', fontdict=self.font)
        plt.bar(city, unit_price_mean, label='元/平米')
        for x, y in enumerate(unit_price_mean):
            plt.text(x, y, y, ha='center')
        plt.legend()

    # 总价最大值与最小值比较
    def total_max_min(self):
        total_price_max = df['total_price'].groupby(df['city']).max()
        city = list(total_price_max.index)
        Max = total_price_max.tolist()
        total_price_min = df['total_price'].groupby(df['city']).min()
        Min = total_price_min.tolist()
        plt.subplot(233)
        plt.title('总价最大值与最小值比较', fontdict=self.font)
        plt.plot(city, Max, 'd-', label='Max/万元')
        for x, y in enumerate(Max):
            plt.text(x, y, y, va='bottom', ha='center')
        plt.plot(city, Min, 'o-', label='Min/万元')
        for x, y in enumerate(Min):
            plt.text(x, y, y, va='bottom', ha='center')
        plt.legend()

    # 单价价最大值与最小值比较
    def unit_max_min(self):
        unit_price_max = df['unit_price'].groupby(df['city']).max()
        city = list(unit_price_max.index)
        Max = unit_price_max.tolist()
        unit_price_min = df['unit_price'].groupby(df['city']).min()
        Min = unit_price_min.tolist()
        plt.subplot(234)
        plt.title('单价最大值与最小值比较', fontdict=self.font)
        plt.plot(city, Max, 'd-', label='Max/元')
        for x, y in enumerate(Max):
            plt.text(x, y, y, va='bottom', ha='center')
        plt.plot(city, Min, 'o-', label='Min/元')
        for x, y in enumerate(Min):
            plt.text(x, y, y, va='bottom', ha='center')
        plt.legend()


def main():
    h = House()
    h.total_price_mean()
    h.unit_price_mean()
    h.total_max_min()
    h.unit_max_min()
    plt.show()


if __name__ == '__main__':
    main()
