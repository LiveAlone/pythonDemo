#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:  多进程的处理方式
'''
import os
from multiprocessing import Process
from multiprocessing import Pool
import random
import time


def fork_create_process():
    """
    通过 fork 方式创建 process 进程方式
    :return: null
    """
    pid = os.fork()
    if pid == 0:
        print 'i am the child process %s and my parent process is %s ' % (os.getpid(), os.getppid())
    else:
        print 'i am the parent process %s and i create the child process is %s' % (os.getpid(), pid)


def sub_process_run(name):
    """
    进程只允许 name 名称参数, 对于 函数 object 参数， 非进程之间的共享
    :param name:
    :return:
    """
    sleep_time = random.randint(1, 10)
    print 'process name: %s, id: %s is start to process, sleep time is %s' % (name, os.getpid(), str(sleep_time))
    time.sleep(sleep_time)
    print 'process name: %s, id: %s is finish to process, sleep time is %s' % (name, os.getpid(), str(sleep_time))


def process_multiple():
    """
    通过 multiprocessing 模块进程的创建方式
    :return: null
    """
    print 'main process start'
    for i in range(1, 11):
        p = Process(target=sub_process_run, args=('child_process_name_' + str(i),))
        p.start()
    print 'main process end'


def process_multiple_pool():
    print 'main process start'
    p = Pool(10)
    for i in range(11):
        p.apply_async(sub_process_run, args=('child_process_name_' + str(i),))
    print 'main process wait finish'
    p.close()
    p.join()
    print 'main process end'


if __name__ == '__main__':
    # fork_create_process()
    # process_multiple()
    # process_multiple_pool()
    process_multiple_pool_ng()






























