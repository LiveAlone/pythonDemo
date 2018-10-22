#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''

if __name__ == '__main__':
    lines = []
    for i in range(1, 100):
        lines.append("this is test condition %s \n" % str(i))
    with open("test.txt", "w") as f:
        f.writelines(lines)
