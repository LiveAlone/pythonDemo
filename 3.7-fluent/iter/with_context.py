#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: is else context 判断方式
'''


# # while else 执行循环判断方式
#
# def validate(my_list):
#     for item in my_list:
#         if item == 'banana':
#             print('i found banana content')
#             break
#     else:
#         raise ValueError('i not found banana exception')
#
# l = ['apple', 'orange', 'grade', 'banana']
# validate(l)


# # try-cache-else except 没有异常产生, else 执行语句， 有异常 不执行 else
#
# def test_block(f):
#     try:
#         f()
#     except ValueError:
#         print('value error content')
#     else:
#         print('else content exec')
#
#
# test_block(lambda : print('hello world'))
#
#
# def f_e():
#     raise ValueError('value error content')
#
#
# test_block(f_e)


# with read 方式 自动资源管理方式

with open('sentence.py') as pt:
    src = pt.read(60)
    print(src)






















