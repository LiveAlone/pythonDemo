#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
description: 函数支持方式
"""

# function 内置函数
# print abs(-123)
# print max(3, 12, 123, 123, 51)


# 函数 支持数据类型校验， 支持函数返回
# def my_fun(x, z=100):
#     if not isinstance(x, (int, long)):
#         raise TypeError('error input error')
#     return -x, x, -z


# print my_fun(100)


# 函数可变参数的配置方式
# def calc1(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
#
# print calc1([1, 2, 3])


# def calc2(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
#
# print calc2(1, 2, 3)
# print calc2(*[1, 2, 3])

# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
#
#
# person('Bob', 35, city='Beijing')
# person('Adam', 45, gender='M', job='Engineer')
#
# # dict 是对应 ** List对应的 * 不同的配置方式
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('Bob', 35, **extra)

# 函数参数的定制
# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# f1(1, 2)
# f1(1, 2, c=3)
# f1(1, 2, 3, 'a', 'b')
# f1(1, 2, 3, 'a', 'b', x=99)
# f1(1, 2, d=99, ext=None)

# 递归函数进行尾递归的简化
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(100))


