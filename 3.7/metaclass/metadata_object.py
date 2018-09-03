#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
description: 通过 metadata 实例 -> 创建 Class -> 通过 Class 创建实例
"""


# list 定义 metaclass 类型支持
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


class MyListSub(MyList):
    pass


# append 方法转换成对应的 add 方法， 支持数据的填充
# L = MyList()
# L.add(1)
# print(L)

L = MyListSub()


