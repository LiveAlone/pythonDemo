#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: splash config user id test
'''
import requests
from random_object_id.random_object_id import gen_random_object_id

SOURCE_RUL = "https://qijunyao.d.xiaohongshu.com/api/sns/v1/system_service/%s/splash_config"
RANDOM_USER_COUNT = 1
PER_USER_REQUEST_COUNT = 2
SAVE_FILE_NAME = 'result.txt'


def get_config_id(user_id, try_count=1):
    url = SOURCE_RUL % user_id
    resp_json = requests.get(url).json()
    ads_groups = resp_json['data']['ads_groups']
    if len(ads_groups) < 1:
        print 'user id : %s get error ads_group info %s' % (user_id, ads_groups)
        if try_count >= 3:
            raise Exception
        else:
            return get_config_id(user_id, try_count + 1)
    return ads_groups[0]['id']


if __name__ == '__main__':
    print 'test condition'

    with open(SAVE_FILE_NAME, 'ab') as f:
        user_result = {}
        for i in range(RANDOM_USER_COUNT):
            user_id = gen_random_object_id()
            except_result = None
            for j in range(PER_USER_REQUEST_COUNT):
                result = get_config_id(user_id)
                if not except_result:
                    except_result = result
                if result != except_result:
                    print 'ERROR user_id: %s, index: %s, call times %s error, expect_result: %s, real_result:%s,' \
                          % (user_id, i, j, except_result, result)
                    raise RuntimeError
                else:
                    print 'SUCCESS user_id: %s, index: %s, call times %s success, expect_result: %s, real_result:%s' \
                          % (user_id, i, j, except_result, result)
            f.write('mock user_id : %s, request count: %s, result: %s SUCCESS \n'
                    % (user_id, PER_USER_REQUEST_COUNT, except_result))
            f.flush()
            count = user_result.get(except_result, 0)
            user_result[except_result] = (count + 1)
        f.write("mock test result count is %s" % str(user_result))
    print 'finish test condition'
