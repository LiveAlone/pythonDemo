#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 扑克牌对象设计
'''

import collections


Card = collections.namedtuple('Card', ['rank', 'suit'])


class Desk(object):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = '方片 黑桃 红桃 梅花'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                       for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __contains__(self, item):
        return item.rank == 'K'


if __name__ == '__main__':
    # beer_card = Card('7', '红桃')
    # print(beer_card)
    desk = Desk()
    # print(len(desk))
    # print(desk[28])
    # print(desk[1:6])
    # print(desk[1::4])
    # for card in desk:
    #     print(card)
    # for card in reversed(desk):
    #     print(card)

    # contains 数据包含支持方式
    print(Card('7', '红桃') in desk)
    print(Card('K', '核桃') in desk)









