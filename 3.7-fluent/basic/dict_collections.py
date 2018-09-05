#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:  字典集合相关模块配置方式
'''

# from _collections_abc import Mapping
#
#
# my_dic = {}
# print(isinstance(my_dic, Mapping))

# # hash eq 共同实现， hash 代替 object, 不可变对象的映射方式; 但是引用对象 保证不可变， 才是可以 散列方式
# tt = (1, 2, (99, 100))
# print(hash(tt))
# t1 = (1, 2, [99, 100])  # 可变对象 不能hash
# print(hash(t1))
# t2 = (1, 2, frozenset([99, 100]))
# print(hash(t2))

# a = dict(one=1, two=2, three=3)
# b = {'one': 1, 'two': 2, 'three': 3}
# c = dict(zip(['two', 'three', 'one'], [2, 3, 1]))
# d = dict([('one', 1), ('three', 3), ('two', 2)])
# e = dict({'one': 1, 'two': 2, 'three': 3})
# print(a == b)
# print(b == c)
# print(c == d)
# print(d == e)

# dic build
# DIAL_CODES = [
#         (86, 'China'),
#         (91, 'India'),
#         (1, 'United States'),
#         (62, 'Indonesia'),
#         (55, 'Brazil'),
#         (92, 'Pakistan'),
#         (880, 'Bangladesh'),
#         (234, 'Nigeria'),
#         (7, 'Russia'),
#         (81, 'Japan'),
# ]
#
# country_code = {country: code for code, country in DIAL_CODES}
# print(country_code)
# print({code: country.upper() for country, code in country_code.items() if code < 66})

# dict 快速失败， 提高 默认值得访问效率
# d = dict()
# d[1] = [1, 2]

# 普通方式
# print(d[1])
# L = d[1]
# L.append(666)
# print(L)
# print(d[1])  # dict 中元素修改
# l_default = d.get(2, [])
# print(l_default)
# l_default.append(777)   # 获取 default 并没有插入 default 中， 下面要重新插入
# print(l_default)
# print(2 in d)
# d[2] = l_default
# print(d[2])

# 默认数据插入方式
# d.setdefault(2, []).append(777)     # 创建 2 默认值 [], 这个默认值， 已经设置进入了 dict 中
# print(d)

# # default list config 配置方式
#
# import collections
#
# index = collections.defaultdict(list)
# print(index[1])
# print(index.get(2))
# index[2].append(666)
# for k, v in index.items():
#     print(k, v)

# collections 操作

# import collections
#
#
# ct = collections.Counter('abcdefghijklmnopqrestuvwxyz')
# print(ct)


# set 集合 取 并集 交集， 通过 运算符号的配置方式， 对应的运算方式
# s = {1, 1, 2, 3, 4, 1, 3, 2}
# print(s)
# print(type(s))















