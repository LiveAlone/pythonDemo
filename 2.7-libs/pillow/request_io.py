#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:  图形图片加载
'''

from PIL import Image
from urllib2 import urlopen
from cStringIO import StringIO

LOAD_IMAGE_URL = 'https://image.baidu.com/search/down?tn=download&word=download&ie=utf8&fr=detail&url=https%3A%2F%2Ftimgsa.baidu.com%2Ftimg%3Fimage%26quality%3D80%26size%3Db9999_10000%26sec%3D1537339056636%26di%3D605f01fb00759070c67993e938418031%26imgtype%3D0%26src%3Dhttp%253A%252F%252Fimg5.duitang.com%252Fuploads%252Fitem%252F201411%252F07%252F20141107164334_2PWXw.jpeg&thumburl=https%3A%2F%2Fss1.bdstatic.com%2F70cFuXSh_Q1YnxGkpoWK1HF6hhy%2Fit%2Fu%3D2049995230%2C1480208359%26fm%3D26%26gp%3D0.jpg'


def main(image_url):
    file = StringIO(urlopen(image_url).read())
    img = Image.open(file)
    img.save('static/random.jpg')


if __name__ == '__main__':
    main(LOAD_IMAGE_URL)
