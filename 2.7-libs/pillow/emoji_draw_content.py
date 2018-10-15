#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''
from PIL import Image, ImageFont, ImageDraw
from emojipy import Emoji

# FONT_PATH = "static/DejaVuSansMono.ttf"
FONT_PATH = "static/Symbola.ttf"
# FONT_PATH = "static/block.ttf"

if __name__ == '__main__':
    # text = u'A\U0001F61FB'
    text = u'含emoji😁🙂😚😎👤🦏🦒➕➕➕👳'
    # text = "It's emoji time \u263A \U0001F61C. Let's add some cool " \
    #           "emotions \U0001F48F \u270C. And some more \u2764 \U0001F436"
    text = Emoji.unicode_to_image(text)
    print(text)
    image = Image.new("RGBA", (1500, 500), (255, 255, 255))
    font = ImageFont.truetype(FONT_PATH, 30, encoding='unic')
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, (0, 0, 0), font=font)
    # image.save("Test.png")
    image.show()
