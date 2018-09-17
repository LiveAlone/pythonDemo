#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 对象的行为模式通过 param 参数判断方式, 通常 static method 通过 _method 方式进行测试
'''


class Catalog(object):
    """
    param 参数方式 判断对象的 行为模式
    """
    def __init__(self, param):
        pass

    @staticmethod
    def _static_method_first():
        print('this is first static method')

    @staticmethod
    def _static_method_second():
        print('this is second static method')

    def main_method(self):
        pass

def main():
    pass


if __name__ == '__main__':
    main()
