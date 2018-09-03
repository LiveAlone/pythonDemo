#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
description: 错误异常消息处理
"""

# try - cache
# try:
#     print(10 / 0)
# except ZeroDivisionError, e:
#     print(e)
# finally:
#     print('finally')


# try:
#     print(10 / 0)
#     # raise Exception('123')
#     # print('None')
# except ZeroDivisionError, e:
#     print(e)
# except ValueError, e:
#     print(e)
# else:
#     print('no error')
# finally:
#     print('finally')

# def fn(x, y):
#     return x / y
#
#
# def qn(x, y):
#     return fn(x, y)
#
#
# print(qn(10, 0))    # 打印出对应的 Exception Track


# logging 错误日志相关, 通过日志打印对应的错误消息
# import logging, sys
#
# logger = logging.getLogger('error_del')
# logger.setLevel(logging.DEBUG)
# format = logging.Formatter("%(asctime)s - %(name)s  "
#                            "- %(levelname)s  "
#                            "- %(funcName)s "
#                            "- %(lineno)d "
#                            "- %(message)s")    # output format
# sh = logging.StreamHandler(stream=sys.stdout)    # output to standard output
# sh.setFormatter(format)
# logger.addHandler(sh)
#
# logger.debug("debug level")
# logger.info("info level")
# logger.warn('warn level')
# logger.error('error level')
# logger.critical('critical level')
#
#
# # def foo(s):
# #     return 10 / int(s)
# #
# #
# # def bar(s):
# #     return foo(s) * 2
# #
# #
# # def main():
# #     try:
# #         bar('0')
# #     except Exception as e:
# #         logging.exception(e)
# #
# #
# # main()
# # print('END')

# assert 通过断言方式， 指定

# def fn(x):
#     assert x > 0, "x not allow limit than 0" # 对于不满足条件 AssertionError 错误跑出
#     print(x)
#
#
# fn(10)
# fn(-100)






























