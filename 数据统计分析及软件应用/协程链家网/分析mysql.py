import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pymysql


class House(object):
    def __init__(self):
        self.font = {
            'color': 'r',
            'size': 13
        }
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            passwd='mysql',
            port=3306,
            db='test',
            charset='utf8'
        )
        self.cur = self.conn.cursor()  # 获取游标

    plt.rcParams['font.family'] = 'simhei'
    plt.rcParams['axes.unicode_minus'] = False

    # 计算各城市二手房平均价格
    def avg_total_price(self):
        avg_price = []
        city_sql = [
            'select sum(total_price)/count("北京") from ershoufang where city="北京"',
            'select sum(total_price)/count("上海") from ershoufang where city="上海"',
            'select sum(total_price)/count("苏州") from ershoufang where city="苏州"',
            'select sum(total_price)/count("南京") from ershoufang where city="南京"',
            'select sum(total_price)/count("成都") from ershoufang where city="成都"'
        ]
        # cur = self.conn.cursor()  # 获取游标
        for sql in city_sql:
            self.cur.execute(sql)
            result = self.cur.fetchone()
            avg_price.append(result[0])
        # self.cur.close()
        # self.conn.close()  # 关闭连接
        # 绘图
        city = ['北京', '上海', '苏州', '南京', '成都']
        plt.title('各城市二手房平均价格', fontdict=self.font)
        plt.bar(city, avg_price, label='万元')
        for x, y in enumerate(avg_price):
            plt.text(x, y, y)
        plt.legend()
        plt.show()

    # 计算各城市二手房（/平米）平均价格
    def avg_unit_price(self):
        avg_price = []
        city_sql = [
            'select sum(unit_price)/count("北京") from ershoufang where city="北京"',
            'select sum(unit_price)/count("上海") from ershoufang where city="上海"',
            'select sum(unit_price)/count("苏州") from ershoufang where city="苏州"',
            'select sum(unit_price)/count("南京") from ershoufang where city="南京"',
            'select sum(unit_price)/count("成都") from ershoufang where city="成都"'
        ]
        for sql in city_sql:
            self.cur.execute(sql)
            result = self.cur.fetchone()
            avg_price.append(result[0])
        # 绘图
        city = ['北京', '上海', '苏州', '南京', '成都']
        plt.title('各城市二手房（/平米）平均价格', fontdict=self.font)
        plt.bar(city, avg_price, label='元')
        for x, y in enumerate(avg_price):
            plt.text(x, y, y)
        plt.legend()
        plt.show()


def main():
    h = House()
    h.avg_total_price()
    h.avg_unit_price()


if __name__ == '__main__':
    main()
