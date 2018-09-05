#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:  集合操作方式
'''

a = dict(one=1, two=2, three=3)
b = {'one':1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('one', 1), ('three', 3), ('two', 2)])
print(a == b)
print(b == c)
print(c == d)








































