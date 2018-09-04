#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''

from math import hypot


class Vector(object):

    def __init__(self, x, y):
        self.x  = x
        self.y  = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __repr__(self):
        return 'Vector(%r, %r) ...' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __str__(self):
        return 'Vector(%r, %r) ... str' % (self.x, self.y)


if __name__ == '__main__':
    v1 = Vector(1, 2)
    v2 = Vector(5, 6)
    print(v2 + v1)
    print(abs(v2))
    print(bool(v1))
    print(bool(Vector(-1, 5)))
    print(v1 * 5)
    print(str(v1))  #



