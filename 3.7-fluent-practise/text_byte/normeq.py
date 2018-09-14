#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''

from unicodedata import normalize


if __name__ == '__main__':
    str1 = '姚启俊'
    print(normalize('NFC', str1))
