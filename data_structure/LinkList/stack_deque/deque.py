#!/usr/bin/env python
# encoding: utf-8

"""
@author: liubo-it
@software: PyCharm Community Edition
@file: deque.py
@time: 2016/5/27 17:45
@annotation: deque
"""


def func():
    pass


class Main(object):
    def __init__(self):
        pass


if __name__ == '__main__':
    # python 内置包含队列的功能
    from collections import deque
    queue = deque([1,2,3])
    queue.append(4)
    queue.append(5)
    print queue.popleft()
    print queue.popleft()

