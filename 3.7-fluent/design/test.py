#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''

l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)
l1.append(100)
l1[1].remove(55)
print(l1)
print(l2)
l2[1] += [33, 22]
l2[2] += (10, 11)   # 注意 tuple 是不可变的对象，对象 += 重建了 id 不同了
print(l1)
print(l2)
