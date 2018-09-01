#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# md5 sha1 加密算法， 防止参数验证签名方式

import hashlib


a = hashlib.md5('how to use md5 in python hashlib?'.encode('utf-8'))
print(a.hexdigest())
