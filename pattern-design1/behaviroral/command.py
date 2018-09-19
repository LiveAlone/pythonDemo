#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description:  命令行模式, 支持命令查看方式
'''

import os
import time


class MoveFileCommand(object):

    def __init__(self, src, dist):
        self._src = src
        self._dist = dist

    def execute(self):
        MoveFileCommand.rename(self._src, self._dist)

    def undo(self):
        MoveFileCommand.rename(self._dist, self._src)

    @staticmethod
    def rename(src, dist):
        print('move file %s to %s content' % (src, dist))
        os.rename(src, dist)


if __name__ == '__main__':
    command_stack = list()
    command_stack.append(MoveFileCommand('foo.txt', 'bar.txt'))
    command_stack.append(MoveFileCommand('bar.txt', 'baz.txt'))
    with open("foo.txt", "w") as f:  # Creating the file
        f.write("hahahahah")

    time.sleep(10)

    # they can be executed later on
    for cmd in command_stack:
        time.sleep(5)
        cmd.execute()

    time.sleep(5)

    # and can also be undone at will
    for cmd in reversed(command_stack):
        time.sleep(5)
        cmd.undo()





