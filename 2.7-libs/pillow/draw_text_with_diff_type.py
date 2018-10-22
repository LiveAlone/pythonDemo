#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:  不同的字体文本输入方式
'''

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter

CHART_PATH = "static/chart.png"
SIMPLE_TTF_PATH = 'static/simple.ttf'


def drop_shadow(image, offset=(5, 5), background=0xffffff, shadow=0x444444, border=8, iterations=3):
    total_width = image.size[0] + abs(offset[0]) + 2 * border
    total_height = image.size[1] + abs(offset[1]) + 2 * border
    back = Image.new(image.mode, (total_width, total_height), background)

    shadow_left = border + max(offset[0], 0)
    shadow_top = border + max(offset[1], 0)
    back.paste(shadow, [shadow_left, shadow_top, shadow_left + image.size[0], shadow_top + image.size[1]])

    n = 0
    while n < iterations:
        back = back.filter(ImageFilter.BLUR)
        n += 1

    image_left = border - min(offset[0], 0)
    image_top = border - min(offset[1], 0)
    back.paste(image, (image_left, image_top))

    return back


if __name__ == '__main__':
    fillcolor = (240, 241, 242)
    shadowcolor = (227, 228, 229)
    im = Image.open(CHART_PATH)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(SIMPLE_TTF_PATH, 80)

    text = u'范冰冰'
    x = 100
    y = 100
    px = 6

    # thin border
    # for cx in range(px):
    #     x, y, z = shadowcolor
    #     newshadowcolor = (x + cx * 2, y + cx * 2, z + cx * 2)
    #     draw.text((x - cx, y), text, font=font, fill=newshadowcolor)
    #     draw.text((x + cx, y), text, font=font, fill=newshadowcolor)
    #     draw.text((x, y - cx), text, font=font, fill=newshadowcolor)
    #     draw.text((x, y + cx), text, font=font, fill=newshadowcolor)
    #
    #     # thicker border
    #     draw.text((x - cx, y - cx), text, font=font, fill=newshadowcolor)
    #     draw.text((x + cx, y - cx), text, font=font, fill=newshadowcolor)
    #     draw.text((x - cx, y + cx), text, font=font, fill=newshadowcolor)
    #     draw.text((x + cx, y + cx), text, font=font, fill=newshadowcolor)

    for i in range(6):
        cx = 6 - i
        newshadowcolor = (227 + 2 * cx, 228 + 2 * cx, 229 + 2 * cx)
        draw.text((x - cx, y), text, font=font, fill=newshadowcolor)
        draw.text((x + cx, y), text, font=font, fill=newshadowcolor)
        draw.text((x, y - cx), text, font=font, fill=newshadowcolor)
        draw.text((x, y + cx), text, font=font, fill=newshadowcolor)
        draw.text((x - cx, y - cx), text, font=font, fill=newshadowcolor)
        draw.text((x + cx, y - cx), text, font=font, fill=newshadowcolor)
        draw.text((x - cx, y + cx), text, font=font, fill=newshadowcolor)
        draw.text((x + cx, y + cx), text, font=font, fill=newshadowcolor)

    draw.text((x, y), text, font=font, fill=fillcolor)

    im.save('static/chart_result.png')
