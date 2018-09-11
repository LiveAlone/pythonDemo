#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: python 不支持多线程的运行方式， 支持单进程方式， 单进程 切换等待方式。
'''

# # yield 获取send data 方式
#
#
# def simple_routine():
#     print('routine start')
#     x = yield
#     print('x value is %s' % x)
#     print('routine end')
#
#
# my_cro = simple_routine()
# print(my_cro)
# next(my_cro)
# my_cro.send('all x content')

# def average

def average():
    total = 0.0
    count = 0
    average_value = None
    while True:
        term = yield average_value
        total += term
        count += 1
        average_value = total / count


av = average()

print(next(av))
print(av.send(100))
print(av.send(120))
print(av.send(140))
print(av.send(160))
print(av.send(250))


























