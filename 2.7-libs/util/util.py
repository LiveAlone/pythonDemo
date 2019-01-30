#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''

import time
import random
import hashlib
from random_object_id.random_object_id import gen_random_object_id


if __name__ == '__main__':
    # requestId = '%s_%s_%s' % (int(time.time()), 'user_id', random.getrandbits(64))
    # print hashlib.md5(requestId).hexdigest()
    print gen_random_object_id()
    di = {1: 1, 2: 2}
    print di.get(3, 666)
