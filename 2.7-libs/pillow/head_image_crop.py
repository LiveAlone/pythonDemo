#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:  头像图片的裁剪拼装方式
'''

from PIL import Image


def image_cron():
    img = Image.open('static/head_image.jpg')
    img2 = img.crop((0, 0, 80, 80))
    img2.save('static/head_image2.jpg')


if __name__ == '__main__':
    image_cron()
