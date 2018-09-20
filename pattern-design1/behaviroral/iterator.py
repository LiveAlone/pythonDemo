#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:  迭代器方式， 对数据的封装
'''


def count_to(count):
    numbers = [x for x in range(1, 100)]
    for number in numbers[:count]:
        yield number


if __name__ == '__main__':
    count_five = lambda: count_to(5)
    count_eleven = lambda: count_to(11)
    # for num in count_five():
    #     print(num)
    for num in count_eleven():
        print(num)

