#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''

import collections


class StrKeyDict(collections.UserDict):

    def __setitem__(self, key, value):
        self.data[str(key)] = value

    def __contains__(self, item):
        return str(item) in item

    def __missing__(self, key):
        if isinstance(key, str):
            raise TypeError('not support str key type')
        return self.data[str(key)]

