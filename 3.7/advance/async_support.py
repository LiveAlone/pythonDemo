#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 支持异步调用函数方式, python async, await resources 等
'''

# 协程 定义使用方式, yield 通过 sender 获取数据， 也是 通过 yield 返回数据信息

#
# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'
#
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n += 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
#
#
# if __name__ == '__main__':
#     c = consumer()
#     produce(c)


# # asyncio 支持 异步调用方式
#
# import asyncio
#
#
# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(5)
#     print("Hello again!")
#
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()

# # threading async异步等待, 可以看到执行都是当线程
#
# import threading
# import asyncio
#
#
# @asyncio.coroutine
# def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread())
#
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# # 单线程 事件驱动 网页内容打印方式
#
# import asyncio
#
#
# @asyncio.coroutine
# def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     # Ignore the body, close the socket
#     writer.close()
#
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# 类似方式 python 3.5+ 提供
# @asyncio.coroutine -> async
# yield -> await
#
# import asyncio
#
#
# # @asyncio.coroutine
# # def hello():
# #     print("Hello world!")
# #     r = yield from asyncio.sleep(1)
# #     print("Hello again!")
#
# async def hello():
#     print('Hello World')
#     await asyncio.sleep(2)
#     print('hello again')
#
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# aio http support
# import asyncio
#
# from aiohttp import web
#
#
# async def index(request):
#     await asyncio.sleep(0.5)
#     return web.Response(body=b'<h1>Index</h1>')
#
#
# async def hello(request):
#     await asyncio.sleep(0.5)
#     text = '<h1>hello, %s!</h1>' % request.match_info['name']
#     return web.Response(body=text.encode('utf-8'))
#
#
# async def init(loop):
#     app = web.Application(loop=loop)
#     app.router.add_route('GET', '/', index)
#     app.router.add_route('GET', '/hello/{name}', hello)
#     srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9090)
#     print('Server started at http://127.0.0.1:9090...')
#     return srv
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()















