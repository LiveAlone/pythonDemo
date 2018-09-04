#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''

# from array import array
#
#
# if __name__ == '__main__':
#     a = array('b', (x for x in range(1, 11)))
#     print(a)
#     print(a[5])


# num_py support

import numpy

print(numpy.arange(12))

a = numpy.arange(12)
a.shape = 3, 4
print(a)
print(a[:, 1])

