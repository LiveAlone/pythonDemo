#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
description: 多线程 多进程的支持方式
"""

# import os
#
# print('process (%s) start ...' % os.getpid())
#
# ps = os.fork()
#
# if ps == 0:
#     print('i am the child (%s), and my parent is (%s)' % (os.getpid(), os.getppid()))
# else:
#     print('i am the parent, i create child is (%s)' % ps)

# Windows 并不支持fork
# 通过 from multiprocessing import Process 来支持跨平台

# from multiprocessing import Process
# import os
#
#
# def run_proc(name):
#     print('run child process %s, (%s)...' % (name, os.getpid()))
#
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()    # 当前进程 等待 p 执行完成后返回执行
#     print('Child process end.')


# from multiprocessing import Pool
# import os, time, random
#
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))    # 添加5个 processor 需要等待线程执行完成
#     print('Waiting for all subprocesses done...')
#     p.close()   # 关闭线程池后 不允许添加最新的线程
#     p.join()    # join 等待线程的执行完成
#     print('All subprocesses done.')

# 子进程输入输出的控制, 子进程控制方式
# import subprocess
#
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)

# 定义输入 输出， 数据类型， 输入输出位置等
# import subprocess
#
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)

# 进程之间相互通讯， python 支持 Queue 队列支持

from multiprocessing import Process, Queue
import os, time, random


def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()













