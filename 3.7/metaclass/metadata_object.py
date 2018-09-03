#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
description: 通过 metadata 实例 -> 创建 Class -> 通过 Class 创建实例
"""


# class ListMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['add'] = lambda self, value: self.append(value)
#         return type.__new__(cls, name, bases, attrs)
#
#
# class MyList(list, metaclass=ListMetaclass):
#     pass
#
#
# # 创建MyList.__new__() 创建方式，
# # 1 准备类创建类对象  2 类名字  3 类继承父类集合  4 类方法集合
#
# L = MyList()
# L.add(1)
# print(L)


