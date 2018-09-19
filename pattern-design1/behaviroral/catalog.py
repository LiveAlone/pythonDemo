#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 对象的行为模式通过 param 参数判断方式, 通常 static method 通过 _method 方式进行测试
'''


class Catalog(object):
    """
    param 参数方式 判断对象的 行为模式
    """
    def __init__(self, param):
        self._static_methods = {'first': self._static_method_first, 'second': self._static_method_second}
        if param in self._static_methods.keys():
            self._param = param
        else:
            raise ValueError('catalog error type support')

    @staticmethod
    def _static_method_first():
        print('this is first static method')

    @staticmethod
    def _static_method_second():
        print('this is second static method')

    def main_method(self):
        self._static_methods[self._param]()


class CatalogInstance(object):

    def __init__(self, param):
        self.x1 = 'x1'
        self.x2 = 'x2'
        if param in self._instance_method_choices:
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    def _instance_method_1(self):
        print("Value {}".format(self.x1))

    def _instance_method_2(self):
        print("Value {}".format(self.x2))

    _instance_method_choices = {'param_value_1': _instance_method_1,
                                'param_value_2': _instance_method_2}

    def main_method(self):
        self._instance_method_choices[self.param].__get__(self)()


class CatalogStatic(object):

    def __init__(self, param):
        if param in self._static_method_choices:
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    @staticmethod
    def _static_method_1():
        print("executed method 1!")

    @staticmethod
    def _static_method_2():
        print("executed method 2!")

    _static_method_choices = {'param_value_1': _static_method_1,
                              'param_value_2': _static_method_2}

    def main_method(self):
        self._static_method_choices[self.param].__get__(None, self.__class__)()


def main():
    # Catalog('first').main_method()
    # Catalog('second').main_method()
    # CatalogInstance('param_value_1').main_method()
    # CatalogInstance('param_value_2').main_method()
    CatalogStatic('param_value_1').main_method()
    CatalogStatic('param_value_2').main_method()


if __name__ == '__main__':
    main()
