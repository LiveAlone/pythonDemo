#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
description: io support
"""

# 文件阅读方式
# try:
#     f = open('test.txt', 'r')
#     print(f.read())
# except Exception, e:
#     print(e)
# finally:
#     if f:
#         f.close()

# 类似 java resource 方式

# with open('test.txt', 'r') as f:
#     print(f.read())
#
# with open('test.txt', 'r') as f:
#     for line in f.readlines():
#         # print(line)
#         print(line.strip()) # 结尾默认添加 \n 注解方式

# File 同时支持文件的读写方式， read write 的读写方式

# StringIO 方式

# from io import StringIO
#
#
# f = StringIO()
# f.write(u'hello')
# f.write(u' ')
# f.write(u'world')
# print(f.getvalue())
#
# f = StringIO(u'Hello!\nHi!\nGoodbye!')
#
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())


# from io import BytesIO
#
# f = BytesIO()
#
# f.write(u'中文'.encode('utf-8'))
#
# print(f.getvalue())

# 操作系统 文件环境配置

import os

# print(os.name)
#
# print(os.uname())
#
# print(os.environ)

# 路径文件系统的拆分
# print(os.path.split('/Users/michael/testdir/file.txt'))
# print(os.path.splitext('/Users/michael/testdir/file.txt'))


# 简洁显示文件路径配置方式等
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

# 数据序列化的支持

# import pickle
#
# d = dict(name='Bob', age=20, score=88)
#
# print(pickle.dumps(d).strip())
#
# s = pickle.dumps(d)
#
# f = dict(name='BobNo', age=120, score=188)
#
# pickle.dump(f, s)
#
# print(f)

# import json
#
# d = dict(name='Bob', age=20, score=88)
#
# sj = json.dumps(d)
#
# print(sj)




