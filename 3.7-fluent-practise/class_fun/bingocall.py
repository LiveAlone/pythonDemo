#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 对象可调用方式
'''

import random


class BingoCase:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('current is lookup error')

    def __call__(self, *args, **kwargs):
        return self.pick()


if __name__ == '__main__':
    bingo = BingoCase(range(1, 5))
    print(bingo())
    print(bingo())
    print(bingo())
    print(bingo())
    callable(bingo)
    print(bingo())










