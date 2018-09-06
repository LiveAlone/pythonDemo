#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''


class Cat:
    def run(self):
        print('cat is running')

    def jump(self):
        print('cat is jump ...')


class DogP:
    def jump(self):
        print('dogP is jump ...')


class Dog(DogP):
    def run(self):
        print('dog is running')


class Dc(Dog, Cat):
    pass


# 继承方式， 当前 object 查找对象， 找不到， 去继承第一个查找， 依次查找， 找不到 向上再去寻找
d = Dc()
d.run()
d.jump()    # 可以看到，先查找第一个继承的父类， 深度遍历方式

print(d.run)
print(d.jump)
Cat.jump(d)  # 可以通过 Cat 显示 class 对象调用方式
