#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 抽象模板方式
'''

from abc import abstractmethod


class Discount:
    @abstractmethod
    def discount(self):
        """ 计算折扣方式 """


class SingleDiscount(Discount):
    def discount(self):
        print('this is single discount')


class MultipleDiscount(Discount):
    def discount(self):
        print('this is not multiple discount')


class DiscountFactory:
    @staticmethod
    def get_discount(is_multiple):
        if is_multiple:
            return MultipleDiscount()
        else:
            return SingleDiscount()


if __name__ == '__main__':
    print(DiscountFactory.get_discount(True).discount())
    print(DiscountFactory.get_discount(False).discount())
