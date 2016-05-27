#!/usr/bin/env python
# encoding: utf-8

"""
@author: liubo-it
@software: PyCharm Community Edition
@file: circular_linked_list.py
@time: 2016/5/27 15:23
@annotation: circular_linked_list
"""


def func():
    pass


class Node(object):
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node


class CircularLinkList(object):
    def __init__(self):
        self.head = None
        self.tail = self.head


if __name__ == '__main__':
    cll = CircularLinkList()

