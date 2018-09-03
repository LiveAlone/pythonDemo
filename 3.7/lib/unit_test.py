#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
description: 单元测试相关支持
"""

# import unittest
# from dict_for_unittest import Dict
#
#
# class TestDict(unittest.TestCase):
#
#     def setUp(self):
#         print('set up ... ')
#
#     def tearDown(self):
#         print('tear down')
#
# # def test_init(self):
#     #     d = Dict(a=1, b='test')
#     #     self.assertEqual(d.a, 1)
#     #     self.assertEqual(d.b, 'test')
#     #     self.assertTrue(isinstance(d, dict))
#     #
#     # def test_key(self):
#     #     d = Dict()
#     #     d['key'] = 'value'
#     #     self.assertEqual(d.key, 'value')
#     #
#     # def test_attr(self):
#     #     d = Dict()
#     #     d.key = 'value'
#     #     self.assertTrue('key' in d)
#     #     self.assertEqual(d['key'], 'value')
#     #
#     # def test_keyerror(self):
#     #     d = Dict()
#     #     with self.assertRaises(KeyError):
#     #         value = d['empty']
#     #
#     # def test_attrerror(self):
#     #     d = Dict()
#     #     with self.assertRaises(AttributeError):
#     #         value = d.empty
#
#
# if __name__ == '__main__':
#     unittest.main()

# 基于文档测试方式


def abs(n):
    '''
    Function to get absolute value of number.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else (-n)


print(abs(100))











