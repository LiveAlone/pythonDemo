#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:  tuple 数据的 分装 拆分方式
'''

# L = (1, 2)
#
# print(L.__class__)
# print(L)
# print(*L)
#
#
# def div_mod(a, b):
#     return a % b
#
#
# print(div_mod(10, 3))
# L = (66, 17)
# print(div_mod(*L))


# 数据组合 拆分， 拼装方式

# a, b, *L = range(1, 100)
# a, b, *L = range(1, 3)
# a, b, *L, d = range(1, 10)
# print(a, b)
# print(L)    # list 数据结构

# _fileds test

# import collections
#
#
# Cs = collections.namedtuple('Coll', 'A B C D')
# c = Cs(1, 2, 3, 4)
# print(c)
# print(Cs._fields)
#
# L = (1, 2, 3)
# print(L)


# L = range(1, 30)
# print(L.__class__)
# print(L)


class A(object):

    def __mul__(self, other):
        print('a multiple')


class B(object):

    def __mul__(self, other):
        print('b multiple')


a = A()
b = B()
a * b
b * a
















