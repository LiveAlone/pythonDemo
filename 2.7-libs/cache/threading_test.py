#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:  多线程的启动方式， 提高单核CPU 的使用占有率
'''

import time, threading


def loop_func(max_count):
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while True:
        n += 1
        if n > max_count:
            break
        print 'thread %s is running in index %s' % (threading.current_thread().name, str(n))
        time.sleep(2)


def threading_test():
    for i in range(1, 6):
        t = threading.Thread(target=loop_func, name='sub thread index : {}'.format(i))
        t.start()


if __name__ == '__main__':
    threading_test()
