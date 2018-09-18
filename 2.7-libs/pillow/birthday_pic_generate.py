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

NAME = u'这就是我的名字'
AGE = 6
ORIGIN_IMAGE_PATH = 'static/bir_origin.png'     # 原始图片的路径
BLOCK_TTF_PATH = 'static/block.ttf'
SIMPLE_TTF_PATH = 'static/simple.ttf'
HEAD_IMAGE_PATH = 'static/head_image.jpg'


def generate_birthday():
    im = Image.open(ORIGIN_IMAGE_PATH)
    draw = ImageDraw.Draw(im)

    # name generate
    name_font = ImageFont.truetype(BLOCK_TTF_PATH, 30)
    draw.text((320, 743), NAME, font=name_font, fill=(0, 0, 0))

    # size block, startIndex:458, 466
    if AGE >= 10:
        age_x = 458
    else:
        age_x = 466
    age_font = ImageFont.truetype(SIMPLE_TTF_PATH, 27)
    draw.text((age_x, 880), str(AGE), font=age_font, fill=(0, 0, 0))

    # head image 扣取中心的 image 图片方式
    head_img = Image.open(HEAD_IMAGE_PATH)
    head_img_size = head_img.size
    x_length = head_img_size[0]
    y_length = head_img_size[1]

    absolute_length = abs(x_length - y_length) // 2
    if x_length < y_length:
        head_img2 = head_img.crop((0, absolute_length, x_length,  absolute_length + x_length))
    else:
        head_img2 = head_img.crop((absolute_length, 0,  absolute_length + y_length, y_length))
    head_img3 = head_img2.resize((210, 210))

    # 中心园内切正方形 PX = 305, PY = 520, a = 140
    # 因此圆中心 o(375, 590) , 半径 r = 105
    # 放置到图片， (270, 485) 的开始位置
    head_image_pim = head_img3.load()
    pim = im.load()
    for PX in range(0, 210):
        for PY in range(0, 210):
            if pow((PX - 105), 2) + pow((PY - 105), 2) < pow(105, 2):
                if pim[270 + PX, 485 + PY] == (255, 255, 255, 255):
                    pim[270 + PX, 485 + PY] = head_image_pim[PX, PY]

    im.save('static/bir_result.png')


if __name__ == '__main__':
    print 'start birthday generate'
    generate_birthday()
    print 'end birthday generate'

