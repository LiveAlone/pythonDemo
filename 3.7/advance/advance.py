#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
description: 切片操作
"""
# L = ['Michael', 'Sarah', 'Tracy']
# print L[-2:]

# 切片对应的 index 的位置， 通过切片快速获取方式
# 通过数组的下标填充方式
# L = list(range(100))
# print L
# print L[:10]
# print L[-10:]
# print L[5:10]
# print L[:11:2]

# 迭代相关操作 实现 Iterable 可迭代
# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
#     print key

# from collections import Iterable
#
# print isinstance('abc', Iterable)
# print isinstance([1, 2, 3], Iterable)
# print isinstance(123, Iterable)

# enumerate 多个元素指定
# print enumerate(['A', 'B', 'C'])
#
# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, value)

# 列表生成器， 生成对应 List 方式
# print range(1, 10)
# print isinstance(range(1, 10), list)
# print list(range(1, 10))
# print [x * x for x in range(1, 11)]
# print [x * x for x in range(1, 11) if x % 2 == 0]
# print [m + n for m in 'ABC' for n in 'XYZ']


# import os
#
# print [d for d in os.listdir('.')]
#
# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# print [k + '=' + v for k, v in d.items()]
#
# L = ['Hello', 'World', 'IBM', 'Apple']
# print [s.lower() for s in L]

# generator 生成器， 没必要 List 类型的迭代

# print([x * x for x in range(10)])
# g = (x * x for x in range(10))
# print(next(g))
# for x in g:
#     print(x)


# 通过 yield 方式 生成 迭代器
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n += 1
#     return 'done'
#
#
# f = fib(6)
# for x in f:
#     print(x)

# iterable 提供支持 for 循环方式， iterator 不仅仅支持 for 循环， 支持 next() 方式
# from collections import Iterable
# from collections import Iterator

# l = [x * x for x in range(10)]
# g = (x * x for x in range(10))
# print(g)
# print(isinstance(g, Iterable))
# print(isinstance(g, Iterator))
# print(l)
# print(isinstance(l, Iterable))
# print(isinstance(l, Iterator))  # false
#
# print(next(g))
# print(next(l))  # Error condition

# iterable 转换成 iterator
# print(isinstance(iter([]), Iterator))
# print(isinstance(iter('abc'), Iterator))





