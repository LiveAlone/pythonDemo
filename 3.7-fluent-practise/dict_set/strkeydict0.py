#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''

import collections


class StrKeyDict0(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError('str type error')
        return self[str(key)]

    def get(self, k, default=None):
        try:
            return self[k]
        except KeyError:
            return default

    def __contains__(self, item):
        return item in self.keys() or str(item) in self.keys()








