#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''

import time


def thread_sleep():
    for i in range(1, 10):
        print i
        time.sleep(1)


if __name__ == '__main__':
    thread_sleep()
