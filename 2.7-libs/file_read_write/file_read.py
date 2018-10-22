#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''

if __name__ == '__main__':
    with open("test.txt", "r") as f:
        lines = f.readlines()
        for l in lines:
            print l.strip()
