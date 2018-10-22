#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''

import os


def test():
    # for root, dirs, files in os.walk("data"):
    #      print root, dirs, files
    if not os.path.isdir('data/test'):
        os.mkdir('data/test')
    for f in os.listdir("data/test"):
        print os.remove("data/%s" % f)


if __name__ == '__main__':
    # test()
    s = '1'
    a = []
    if not s:
        print 'test s is not condition'
