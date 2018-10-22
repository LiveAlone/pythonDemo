#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: 
'''

import datetime
import time
from dateutil.relativedelta import relativedelta


def day_range_iter(begin_date, end_date):
    begin_day = begin_date
    end_day = begin_date + datetime.timedelta(days=1)
    while end_day <= end_date:
        yield (begin_day, end_day)
        begin_day = end_day
        end_day = end_day + datetime.timedelta(days=1)


if __name__ == '__main__':
    # start_date = datetime.datetime(*(2018, 7, 1))
    # end_date = datetime.datetime(2018, 8, 1)
    # print(start_date.month)
    # dr_iter = day_range_iter(start_date, end_date)
    # for kd in dr_iter:
    #     print kd
    # now_date_time = datetime.datetime(2018, 9, 19)
    # before_date_time = datetime.datetime(2018, 9, 16)
    # print (now_date_time - before_date_time).total_seconds()
    # print relativedelta(months=+2)
    # print (datetime.datetime.now() + relativedelta(months=-2))
    # print datetime.datetime.now()
    # print datetime.datetime.now() + datetime.timedelta(days=-1) + datetime.timedelta(minutes=-1)
    # ts = 1518158402
    # time_array = time.localtime(ts)
    # print datetime.datetime.now() - datetime.datetime.fromtimestamp(ts)
    str = datetime.datetime.now().strftime('%Y-%m-%d')
    date = datetime.datetime.strptime('2018-09-27', '%Y-%m-%d')
    print int(time.mktime(date.timetuple())) * 1000
    print str, date

