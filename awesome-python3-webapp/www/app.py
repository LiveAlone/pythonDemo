#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:  app 启动 demo 方式
'''

import logging;logging.basicConfig(level=logging.INFO)
import asyncio,os,json,time
from datetime import datetime
from aiohttp import web


def index(request):
    return web.Response(body=b'<h1> hello index context <h1/>')


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('get', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9090)
    logging.info('server start at 127.0.0.1:9090')
    return srv


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()

