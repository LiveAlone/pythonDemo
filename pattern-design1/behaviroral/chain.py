#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:  chain 
'''

import abc


class Handler(object):

    def __init__(self, successor=None):
        self._successor = successor

    @abc.abstractmethod
    def _handler(self, request):
        raise NotImplementedError('handler not implement error')


