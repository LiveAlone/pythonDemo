#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''

from www import orm
from www.models import User
import asyncio


def test():

    loop = asyncio.get_event_loop()
    cp = orm.create_pool(loop, user='root', password='anywhere', database='awesome')
    loop.run_until_complete(cp)

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    loop.run_until_complete(u.save())
    loop.run_forever()  # 事件方式循环获取对应的 Data 数据信息


if __name__ == '__main__':
    test()
