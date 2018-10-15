#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''
from PIL import Image, ImageFont, ImageDraw


if __name__ == '__main__':
    text = u"test 🤓🤓🤓" #CYCLONE emoji
    image = Image.new("RGBA", (500, 500), (255, 255, 255))
    font = ImageFont.truetype("static/DejaVuSansMono.ttf", 60, encoding='unic')
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, (0, 0, 0), font=font)
    image.save("Test.png")
    image.show()
