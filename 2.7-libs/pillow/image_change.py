#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: test.jpg 图片处理方式
'''

from PIL import Image
from PIL import ImageFilter


def wrap_path(image_name):
    return 'static/' + image_name


def change_size():
    im = Image.open(wrap_path('test.jpg'))
    w, h = im.size
    print('Original image size: %sx%s' % (w, h))
    im.thumbnail((w // 2, h // 2))
    print('Resize image to: %sx%s' % (w // 2, h // 2))
    im.save(wrap_path('thumbnail.jpg'), 'jpeg')


def change_filter():
    im = Image.open(wrap_path('test.jpg'))
    im2 = im.filter(ImageFilter.BLUR)
    im2.save(wrap_path('blur.jpg'), 'jpeg')


if __name__ == '__main__':
    # change_filter()
    change_size()

