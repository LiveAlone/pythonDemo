#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

__author__ = 'yaoqijun'


def test():
    args = sys.argv
    if len(args) == 1:
        print 'hello world!'
    elif len(args) == 2:
        print 'hello world 2'
    else:
        print 'too many args'

if __name__ == '__main__':
    test()
