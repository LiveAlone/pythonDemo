#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:  通过线程池方式， 进行任务分配， 多任务的执行方式, 通过阻塞队列方式， 进行多任务的分发操作。
main 线程判断是否为空， 等待子线程执行完成, 标识当前
'''

import os
from multiprocessing import Pool
from multiprocessing import Queue
import time
import random

MSG_QUEUE = Queue(10)


def worker_process_fun(name):
    """
    多进程 worker 函数执行方式
    :param name: 名称
    :param q: 消息队列
    :return:
    """
    while True:
        task_dict = MSG_QUEUE.get()
        if task_dict['last']:
            break
        task = task_dict['task']
        if name % 2 == 0 and task > 80:
            print 'worker-%s, pid: %s is error task %s' \
                  % (str(name), os.getpid(), str(task))
            # error raise 当前进程取消执行, 等待执行完成
            raise RuntimeError()
        work_time = random.randint(5, 11)
        time.sleep(work_time)
        print 'worker-%s, pid: %s is finish the task %s with process time %s'\
              % (str(name), os.getpid(), str(task), str(work_time))


if __name__ == '__main__':
    p = Pool(5)
    for i in range(5):
        p.apply_async(func=worker_process_fun, args=(i, ))
    print 'Master to put task'
    for i in range(1, 20):
        MSG_QUEUE.put({'task': i, 'last': False})
        print 'Master put task %s finish all' % str(i)
    for i in range(5):
        MSG_QUEUE.put({'task': i, 'last': True})
    print 'Master finish all task'
    while True:
        if MSG_QUEUE.empty():
            p.close()
            p.join()
            break
        else:
            print 'Master not stop all, sleep time wait'
            time.sleep(1)
    print 'Master finish'

