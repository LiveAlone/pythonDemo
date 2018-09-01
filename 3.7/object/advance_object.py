#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __slots__
# class Student(object):
#     pass
#
# def set_age(self, age):
#     self.age = age
#
# s = Student()
# s.name = 'miracle'
# print(s.name)
#
# # 对象方法 绑定
#
# from types import MethodType
#
# s.set_age = MethodType(set_age, s)
# s.set_age(33)
# print(s.age)
#
# s2 = Student()
# s2.set_age(66)  # error called

# # 绑定对应的属性方式
# class Student(object):
#     __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
#
# s = Student()
# s.score = 100   # error, 仅仅通过加入 slots 属性设置绑定

# 通过 @Property @score.setter 方式，decorator 修饰方式
# 通过 Python 内置方法 自定义解释器的执行方式
# class Student(object):
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#
# s = Student()
# s.score = 10
# print(s.score)
# s.score = 120

# # __str__ 类似 java toString() 方式
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'Student is %s' % self.name
#
# s = Student('localhost')
# print(s)
# print(Student('yaoqijun'))


# 通过 Iterable 循环遍历方式
# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1 # 初始化两个计数器a，b
#
#     def __iter__(self):
#         return self # 实例本身就是迭代对象，故返回自己
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b # 计算下一个值
#         if self.a > 100000: # 退出循环的条件
#             raise StopIteration()
#         return self.a # 返回下一个值
#
# for n in Fib():
#     print(n)

# __getitem__ 通过数组方式 获取对象
# class Fib(object):
#     def __getitem__(self, n):
#         a, b = 1, 1
#         for x in range(n):
#             a, b = b, a + b
#         return a
#
# f = Fib()
# print(f[10])

# __getitem__ 切片方法的支持
#
# class Fib(object):
#     def __getitem__(self, n):
#         if isinstance(n, int): # n是索引
#             a, b = 1, 1
#             for x in range(n):
#                 a, b = b, a + b
#             return a
#         if isinstance(n, slice): # n是切片
#             start = n.start
#             stop = n.stop
#             if start is None:
#                 start = 0
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a + b
#             return L
#
# f = Fib()
# print(f[0:5])


# getattr setattr delattr 不同的判定方式
# 通过 __getattr__ 方法方式

# __call__ 对象本身方法的调用
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self):
#         print('My name is %s.' % self.name)
#
# s = Student('Michael')
# s()


# 通过 callable(Student()) 方式判断可用性
# print(callable(max))
# print(callable([1, 2, 3]))
# print(callable(None))
# print(callable('str'))

# 通过枚举判断方式

from enum import Enum, unique

# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)
#
# print(Month.Jan)

# @unique
# class Weekday(Enum):
#     Sun = 0 # Sun的value被设定为0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
#
# print(Weekday.Mon)
# print(Weekday.Sun.value)
# print(Weekday(3))

# 定义元函数方式, 动态语言 ， 运行时刻， 定义的 Class
#
# class Hello(object):
#     def hello(self, name='world'):
#         print('Hello, %s.' % name)

# 下面自定义 Class 内容
# 1 class 名称 2 class 继承类 3 函数绑定名称
# def fn(self, name='world'): # 先定义函数
#     print('Hello, %s.' % name)
#
# Hello = type('Hello', (object,), dict(hello=fn))
#
# h = Hello()
# print(h.hello('yaoqijun'))

# 通过 metaclass 定义 类型






