#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:  插入数据
'''

import pymysql

if __name__ == '__main__':
    db = pymysql.connect("localhost", "root", "anywhere", "awesome")
    cursor = db.cursor()
    cursor.execute("select * from users")
    data = cursor.fetchone()
    print("Database version : %s " % data[0])
    db.close()











