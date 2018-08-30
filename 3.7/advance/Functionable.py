#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
description: 函数式编程, 支持高阶函数方式
"""

# 高阶函数执行方式
# def add(x, y, f):
#     return f(x) + f(y)
#
# print(add(-100, -200, abs))

# map reduce filter sorted 过滤执行方式
#
# def f(x):
#     return x*x
#

# map 的结果 是一个 Iterator 需要遍历执行方式
# print(list(map(f, [1, 2, 3, 4, 5])))

# reduce 不同， map 是 iterator, reduce 是 立即执行方式
# from functools import reduce
# def add(x, y):
#     return x + y
#
# print(reduce(add, [1, 2, 3, 4, 5]))

# map reduce 通过 lambda 简洁的表达方式
#
# from functools import reduce
#
# # def fn(x, y):
# #     return x + 10 + y
# #
# # def char2num(s):
# #     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# #     return digits[s]
# #
# # print(reduce(fn, map(char2num, '13579')))
#
# # 简介版本支持
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
# print(reduce(lambda x, y: x+y, map(lambda x:DIGITS[x], '13579')));

# filter 支持过滤的配置方式, filter 也是 iterator 的过滤方式
# print(list(filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6, 7])))

# # demo 素数生产工厂
# def _odd_iter():
#     n = 1
#     while True:
#         n += 2
#         yield n
#
# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(lambda x: x%n>0, it)
#
# # 上面就是 primes  优化器， 会吧 每个 prime， 合数过滤掉
# 不知道 prime 函数底层实现方式

# sort 支持排序方式
# print(sorted([36, 5, -12, 9, -21], key=abs))
# 类似 compare 方式， 通用转换方式, 通过转换后 排序方式。

# 函数返回值， 返回待执行的 fun
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
# f = lazy_sum(1, 3, 5, 7, 9)
# f2 = lazy_sum(1, 3, 5, 7, 9)
# print(f)
# print(f())
# print(f == f2)

# 闭包的原因，引用函数原始, 知道 f1, f2, f3 执行时候， 引用外部 i,
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
#
# f1, f2, f3 = count()
# print(f1(), f2(), f3())

# g1 g2 g3，指向的 f, f -> i, 每次执行 对应 i 保存,
# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs
#
# g1, g2, g3 = count()
# print(g1(), g2(), g3())

# 匿名函数 lambda 类是上面的表达方式

# 修饰器 wrapper, 对应函数执行了一层封装
#
# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
# @log
# def now():
#     print('2015-3-25')
#
# now()

#对应 修饰器的封装方式
# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
# @log('execute')
# def now():
#     print('2015-3-25')
#
# # 类似方式 now = log('execute')(now)
# # now()
# print(now.__name__) # wrapper 方式

# func wrapper

# import functools
#
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
# @log
# def now():
#     print('2015-3-25')
#
# now()
# # wrapper.__name__ = func.__name__
# print(now.__name__) # 因为注解封装， 是 wrapper 方法 functions.wraps() 对应分装 __name__ 还是 now


# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
# @log('execute')
# def now():
#     print('2015-3-25')
#
# now()
# print(now.__name__)

# 偏函数， 类是函数默认参数转换

# def add_plus(x, y, c):
#     return x * c + y
#
# print(add_plus(9, 5, 100))
#
# import functools
#
# add_plus_10 = functools.partial(add_plus, c = 10)
# print(add_plus_10(9, 5))









