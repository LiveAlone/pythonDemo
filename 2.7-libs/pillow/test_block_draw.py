#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:  图片对应的 block 内容的写入方式
'''

from PIL import Image

# 中心 o(375, 590)

o = (375, 590)
r = 99
PX = o[0] - r
PY = o[1] - r
a = 2 * r

# PX = 305    # x 轴位置
# PY = 520    # y 轴位置
# a = 140     # 边长
PXE = PX + a
PYE = PY + a



def draw_block():
    img = Image.open('static/test.jpg')
    # print img.size
    pim = img.load()
    for x in range(PX, PXE + 1):
        for y in range(PY, PYE + 1):
            pim[x, y] = (0, 0, 0)
    img.save('static/test_lt.jpg')



def draw_test_block():
    img = Image.open('static/bir_origin.png')
    pim = img.load()
    for x in range(PX, PXE + 1):
        for y in range(PY, PYE + 1):
            pim[x, y] = (0, 0, 0)
    img.save('static/bir_origin_test.png')



if __name__ == '__main__':
    draw_test_block()














