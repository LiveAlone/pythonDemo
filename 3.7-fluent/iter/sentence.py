#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:  单词序列配置方式
'''

# import re
# import reprlib
#
#
# RE_WORD = re.compile('\w+')
#
# class Sentence:
#
#     def __init__(self, text):
#         self.text = text
#         self.words = RE_WORD.findall(text)
#
#     def __getitem__(self, item):
#         return self.words[item]
#         # return 'yaoqijun'
#
#     def __len__(self, other):
#         return len(self.words)
#
#     def __repr__(self):
#         return 'Sentence(%s) ' % reprlib.repr(self.text)
#
# if __name__ == '__main__':
#     s = Sentence('programmer can use to solve common problems when designing an application')
#     # for word in s:
#     #     print(word)
#     print(s[15])


# # iterable iterator 不同的 迭代器方式
#
# from typing import Iterable, Iterator
#
# s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# # print(isinstance(s, Iterable))
# # for char in s:
# #     print(char)
#
#
# # iterator 迭代器方式 遍历循环
#
# s_iter = iter(s)
# # print(isinstance(s_iter, Iterator))
# while True:
#     try:
#         print(next(s_iter))
#     except StopIteration:
#         print("stop iteration")
#         break

# yield stop 方式


def gen_AB():
    print("start")
    yield 'A'
    print('continue')
    yield 'B'
    print('end')

# gen = gen_AB()
# print(gen)
# print(next(gen))
# print(next(gen))
#
# try:
#     print(next(gen))
# except StopIteration:
#     print('all expect end')


# l = [x for x in gen_AB()]
# it = (x for x in gen_AB())  # 注意这里是一个 迭代器哦， typle 都是 迭代器方式
# print(l)
# print(it)
# print(next(it))


# yield from 支持 index 返回方式

# def chain(*its):
#     for it in its:
#         for i in it:
#             yield i
#
# s = 'ABCD'
# t = tuple(range(4))
# print(list(chain(s, t)))
#
# def chain(*its):
#     for it in its:
#         yield from it
#
# s = 'ABCD'
# t = tuple(range(4))
# print(list(chain(s, t)))


# # iter 第一个参数 可调用对象， 第二个 哨兵方式， 判断相同
# from random import randint
#
# def d6():
#     return randint(1, 6)
#
# # print(d6())
#
# d6_iter = iter(d6, 1)
#
# print(d6_iter)
# for i in d6_iter:
#     print(i)











