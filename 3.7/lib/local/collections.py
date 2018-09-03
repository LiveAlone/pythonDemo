#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# # namedtuple 不可变的对象封装方式
#
# from collections import namedtuple
#
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)
#
# print(p.x, p.y)
# # p.x = 100 # Error can not set the value


# list 的线性 结构， 访问速度快， 插入删除慢
#
# from collections import deque
#
# q = deque(['a', 'b', 'c'])
# q.append('x')
# print(q)
# q.appendleft('y')
# print(q)

# # defaultDict dict 数据类型，返回默认的数值
#
# from collections import defaultdict
#
# dd = defaultdict(lambda : 'default')
#
# dd['key1'] = 'aaa'
#
# print(dd)
# print(dd['key1'])
# print(dd['key2'])

# # ordered dict 有序的 dict 集合配置方式
#
# from collections import OrderedDict
#
# d =dict()
# d['z'] = 1
# d['x'] = 3
# d['y'] = 2
# print(d.keys())
#
# od = OrderedDict()
# od['z'] = 1
# od['x'] = 2
# od['y'] = 3
# print(od.keys())


# counter test 配置方式
from collections import Counter

c = Counter()

for ch in 'programmer python test':
    c[ch] += 1

print(c)





























