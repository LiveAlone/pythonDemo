#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 面向对象编程方式
#
# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print('%s : %s'%(self.name, self.score))
#
# yao = Student('yao', 99)
# lisa = Student('lisa', 66)
# yao.print_score()
# lisa.print_score()
# print(yao)

# yao.name = 'qijun'
# yao.print_score()


# 访问的限制 通过 __field 方式， 限制访问

# class Student(object):
#
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#         self._age = 18
#
#     def print_score(self):
#         print('%s - %s'%(self.__name, self.__score))
#
#     def set_score(self, score):
#         if score > 100:
#             raise ValueError('score not more than 100')
#         self.__score = score
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_age(self, age):
#         self._age = age
#
#     def print_score_age(self):
#         print('%s - %s - %s'%(self.__name, self.__score, self._age))
#
# yao = Student('yao', 99)
# # yao.print_score()
# # print(yao.__name)   # error
# # yao.set_name('qijun')
# # yao.print_score()
#
# print(yao._age) # 应当是 protected, 默认不允许访问的
# yao.print_score_age()

# # 继承 多态，面向对象的编程方式
#
# class Animal(object):
#
#     def run(self):
#         print('Animal is running')
#
# class Dog(Animal):
#
#     def run(self):
#         print('Dog is running')
#
#
# class Cat(Animal):
#
#     def run(self):
#         print('Cat is running')
#
# d = Dog()
# d.run()
#
# c = Cat()
# c.run()
#
# print(isinstance(d, Animal))
# print(isinstance(c, Animal))
#
# # python 是 run 动态语言，只要是 run 支持， var 不用指定对应运行类型。
# def run_again(x):
#     x.run()
#     x.run()
#
# run_again(d)

# 对象属性 信息获取方式

# type 获取对象信息
# print(type(123))
# print(type('str'))
# print(type(type(666)))
# print(type(123) == int)
# print(type('str') == str)

# # types 引入对象类型判断
#
# import types
#
# def fn():
#     pass
#
# print(type(fn))
# print(type(fn) == types.FunctionType)
# print(type(abs))
# print(type(abs) == types.BuiltinFunctionType)
# print(lambda x : x + y)
# print(type(lambda x : x) == types.LambdaType)
# print((x for x in range(1, 10)))
# print(type(x for x in range(1, 10)) == types.GeneratorType)

# # 对于 Type 类型 仅仅支持 获取对象的类型，通过 isInstance 方式， 判断对象继承关系
# from collections import Iterable
# L = [1, 2, 3, 4]
# print(type(L))
# print(isinstance(L, Iterable))

# # 对象的 其他属性
# print(dir('ABC'))   # dir 获取对象所有属性
# print('ABC'.__len__())
#
# class MyObject(object):
#     def __init__(self, x):
#         self.x = x
#
#     def power(self):
#         return self.x * self.x
#
# o = MyObject(9)
# # print(o.power())
# # print(hasattr(o, 'x'))
# # print(hasattr(o, 'y'))
# # setattr(o, 'y', 100)
# # print(hasattr(o, 'y'))
# # print(getattr(o, 'y'))
# # print(o.y)
# # print(getattr(o, 'z'))
# power = getattr(o, 'power')
# print(power())

# 静态属性配置方式
# class Student(object):
#     name = 'Student'
#
# s = Student()
# t = Student()
# print(s.name)
# print(t.name)
# print(Student.name)
#
# s.name = 'yaoqijun' # 属性的优先级, 比 普通的对象 优先级高， Student.name 熟悉被覆盖的
# print(s.name)
# print(t.name)
# print(Student.name)













