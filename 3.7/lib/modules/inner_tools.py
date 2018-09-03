#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
description: 常用的内建模块
"""

# # datetime
#
# from datetime import datetime
#
# print(datetime.now())
# print(type(datetime.now()))
#
# print(datetime(2015, 4, 19, 12, 20))
#
# # 相对 datetime 类型， timestamp
# # timestamp 不区分时区， datetime 记录时区相关属性
# print(datetime.now().timestamp())

# 时区转换
from datetime import datetime
print(datetime.fromtimestamp(1429417200.0))  # 本地时间
print(datetime.utcfromtimestamp(1429417200.0))  # uct 时间

print(datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S'))
print(datetime.now().strftime('%a, %b %d %H:%M'))

