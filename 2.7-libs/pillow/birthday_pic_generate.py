#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:  生成用生日图片查看
'''
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

NAME = u''
AGE = 58


def generate_birthday():
    im = Image.open('static/bir_origin.png')
    draw = ImageDraw.Draw(im)

    # name generate
    name_font = ImageFont.truetype('static/block.ttf', 30)
    draw.text((320, 743), NAME, font=name_font, fill=(0, 0, 0))

    # size block, startIndex:458, 466
    if AGE >= 10:
        age_x = 458
    else:
        age_x = 466
    age_font = ImageFont.truetype('static/simple.ttf', 27)
    draw.text((age_x, 880), str(AGE), font=age_font, fill=(0, 0, 0))

    # head image save

    im.save('static/bir_result.png')


if __name__ == '__main__':
    print 'start birthday generate'
    generate_birthday()
    print 'end birthday generate'

