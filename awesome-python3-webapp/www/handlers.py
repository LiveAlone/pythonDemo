#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:  route handle 请求处理方式
'''

from www.coroweb import get
import re, time, json, logging, hashlib, base64, asyncio
from www.models import User, Comment, Blog, next_id


@get('/')
async def index(request):
    users = await User.find_all()
    return {
        '__template__': 'test.html',
        'users': users
    }

