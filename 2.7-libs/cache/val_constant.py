#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''
import datetime
import time

if __name__ == '__main__':
    # print(5 // 6)
    # print(pow(5, 2))
    # print((1, 2) == (1, 2))
    now = datetime.datetime.now()
    time.sleep(3)
    print (datetime.datetime.now() - now).seconds
