#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''

import datetime


def day_range_iter(begin_date, end_date):
    begin_day = begin_date
    end_day = begin_date + datetime.timedelta(days=1)
    while end_day <= end_date:
        yield (begin_day, end_day)
        begin_day = end_day
        end_day = end_day + datetime.timedelta(days=1)


if __name__ == '__main__':
    start_date = datetime.datetime(*(2018, 7, 1))
    end_date = datetime.datetime(2018, 8, 1)
    print(start_date.month)
    # dr_iter = day_range_iter(start_date, end_date)
    # for kd in dr_iter:
    #     print kd

