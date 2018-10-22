#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''

if __name__ == '__main__':
    num = 20
    l = []
    for i in range(1, 3):
        l.append(i)
    print [l[i::num] for i in range(num)]

