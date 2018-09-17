#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:  图片对应的 block 内容的写入方式
'''

from PIL import Image

PX = 10
PY = 10
PXE = 150
PYE = 150


def draw_block():
    img = Image.open('static/test.jpg')
    # print img.size
    pim = img.load()
    for x in range(PX, PXE + 1):
        for y in range(PY, PYE + 1):
            pim[x, y] = (0, 0, 0)
    img.save('static/test2.jpg')


if __name__ == '__main__':
    draw_block()


