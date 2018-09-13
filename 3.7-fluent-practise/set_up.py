#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''

from dict_set.strkeydict import StrKeyDict


if __name__ == '__main__':
    sk = StrKeyDict()
    sk[1] = '123'
    sk[2] = '456'
    print(sk[2])


