#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''
import gevent
from gevent.queue import Queue

tasks = Queue()


def worker(n):
    while not tasks.empty():
        task = tasks.get()
        print('Worker %s got task %s' % (n, task))
        gevent.sleep(2)

    print('Quitting time!')


def boss():
    for i in xrange(1, 25000):
        tasks.put_nowait(i)
    print 'put finish all content'


if __name__ == '__main__':
    gevent.spawn(boss).join()
    # gevent.joinall([
    #     gevent.spawn(worker, 'steve'),
    #     gevent.spawn(worker, 'john'),
    #     gevent.spawn(worker, 'nancy'),
    #     gevent.spawn(worker, 'steve'),
    #     gevent.spawn(worker, 'john'),
    #     gevent.spawn(worker, 'nancy'),
    #     gevent.spawn(worker, 'steve'),
    #     gevent.spawn(worker, 'john'),
    #     gevent.spawn(worker, 'nancy'),
    #     gevent.spawn(worker, 'steve'),
    #     gevent.spawn(worker, 'john'),
    #     gevent.spawn(worker, 'nancy'),
    #     gevent.spawn(worker, 'steve'),
    #     gevent.spawn(worker, 'john'),
    #     gevent.spawn(worker, 'nancy'),
    # ])
    gevent.spawn(worker, 'steve')
    gevent.spawn(worker, 'john')
    gevent.spawn(worker, 'nancy')
    gevent.spawn(worker, 'steve')
    gevent.spawn(worker, 'john')
    gevent.spawn(worker, 'nancy')
    gevent.spawn(worker, 'steve')
    gevent.spawn(worker, 'john')
    gevent.spawn(worker, 'nancy')
    gevent.spawn(worker, 'steve')
    gevent.spawn(worker, 'john')
    gevent.spawn(worker, 'nancy')
    gevent.spawn(worker, 'steve')
    gevent.spawn(worker, 'john')
    gevent.spawn(worker, 'nancy')
    print "over"
