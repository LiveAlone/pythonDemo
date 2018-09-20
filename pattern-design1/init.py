#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''


class Person(object):

    name = 'abc'

    def __get__(self, instance, owner):
        print(instance)
        print(owner)
        return self

    def __getattribute__(self, item):
        print('getattribute item : ', item)
        return 'getattribute'

    def __getattr__(self, item):
        print('get attr item', item)
        return 'getattr'


class Student(object):
    p = Person()


if __name__ == '__main__':
    s = Student()
    print(s.p.name)
