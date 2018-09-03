#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
description: thread 线程处理方式
"""

# import time, threading
#
#
# def loop():
#     print('thread %s is running ....' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         print('thread %s is running in %s' % (threading.current_thread().name, n))
#         n += 1
#         time.sleep(1)
#
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')    # threading 创建线程数量
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)


# Lock 加锁支持，类似 java lock 控制在线程上

import time, threading

# # 假定这是你的银行存款:
# balance = 0
# lock = threading.Lock()
#
#
# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n
#
#
# def run_thread(n):
#     for i in range(100000):
#         # change_it(n)
#         # 先要获取锁:
#         lock.acquire()
#         try:
#             # 放心地改吧:
#             change_it(n)
#         finally:
#             # 改完了一定要释放锁:
#             lock.release()
#
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# ThreadLocal 多线程划分可用性
# 通过 local 方式支持， 获取当前线程本地变量的支持

# import threading
#
#
# local_school = threading.local()
#
#
# def process_student():
#     # 获取当前线程关联的student:
#     std = local_school.student
#     print('Hello, %s (in %s)' % (std, threading.current_thread().name))
#
#
# def process_thread(name):
#     # 绑定ThreadLocal的student:
#     local_school.student = name
#     process_student()
#
#
# t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# processor 多进程处理方式， multi process 支持不同的机器， 分布式 process 处理方式

