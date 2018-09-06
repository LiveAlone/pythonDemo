#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:  策略模式设计方式
'''

from abc import ABC, abstractclassmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name, fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price


class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

class Promotion(ABC):

    @abstractclassmethod
    def discount(self, order):
        """
        :param order: 计算对应的折扣金额
        :return:
        """

class FidelityPromo(Promotion):
    def discount(self, order):
        return order.total() * 0.5 if order.customer.fidelity >= 1000 else 0



