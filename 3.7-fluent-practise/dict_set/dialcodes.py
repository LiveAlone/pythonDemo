#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 输出dict， == 方式 判断 Value 方式
'''

DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan'),
    ]

if __name__ == '__main__':
    d1 = dict(DIAL_CODES)
    # print(d1)
    d2 = dict(sorted(DIAL_CODES))
    # print(d2)
    d3 = dict(sorted(DIAL_CODES, key=lambda x: x[1]))
    # print(d3)
    # print(d1 == d2)
    # print(d2 == d3)
    # print(d3 == d1)
    # d1[66] = '123'
    # print(d1 == d2)



