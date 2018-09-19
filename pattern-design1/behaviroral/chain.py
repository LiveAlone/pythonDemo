#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:  chain, Client 通过引用方式，职责链方式。 coroutine 路由方式, yield 
'''

import abc
import time


class Handler(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        result = self._handler(request)
        if not result:
            self._successor.handle(request)

    @abc.abstractmethod
    def _handler(self, request):
        raise NotImplementedError('handler not implement error')


class ConcreteHandler1(Handler):

    def _handler(self, request):
        if 0 <= request < 10:
            print('request {} handle in handler in 1'.format(request))
            return True


class ConcreteHandler2(Handler):

    def _handler(self, request):
        if 10 <= request < 20:
            print('request {} handle in handler in 2'.format(request))
            return True


class ConcreteHandler3(Handler):

    def _handler(self, request):
        if 20 <= request < 30:
            print('request {} handle in handler in 3'.format(request))
            return True


class DefaultHandler(Handler):

    def _handler(self, request):
        print('request {} no handler , user default'.format(request))
        return True


class Client(object):

    def __init__(self):
        self._handler = ConcreteHandler1(ConcreteHandler2(ConcreteHandler3(DefaultHandler())))

    def handle_requests(self, requests):
        for request in requests:
            self._handler.handle(request)


def routine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start


@routine
def routine1(target):
    while True:
        request = yield
        if 0 <= request < 10:
            print('routine1 hand the request content: {}'.format(request))
        else:
            target.send(request)


@routine
def routine2(target):
    while True:
        request = yield
        if 10 <= request < 20:
            print('routine2 had the request content: {}'.format(request))
        else:
            target.send(request)


@routine
def routine3(target):
    while True:
        request = yield
        if 20 <= request < 30:
            print('routine3 had the request content: {}'.format(request))
        else:
            target.send(request)


@routine
def routine_default():
    while True:
        request = yield
        print('routine default has the request content: {}'.format(request))


class ClientRoutine(object):

    def __init__(self):
        self.target = routine1(routine2(routine3(routine_default())))

    def handle_requests(self, requests):
        for request in requests:
            self.target.send(request)


def timeit(func):
    def count(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        count._time = time.time() - start
        return res
    return count


if __name__ == '__main__':
    requests_args = [x * 10 for x in range(1, 8)]
    client1 = Client()
    # client1.handle_requests(requests)
    print('-' * 50)
    client2 = ClientRoutine()
    # client2.handle_requests(requests)
    requests_args *= 10000
    client1_delegate = timeit(client2.handle_requests)
    client2_delegate = timeit(client2.handle_requests)
    client1_delegate(requests_args)
    client2_delegate(requests_args)
    print(client1_delegate._time, client2_delegate._time)


















