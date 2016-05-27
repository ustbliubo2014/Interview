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
        self.next_node = next_node


class CircularLinkList(object):
    def __init__(self):
        self.head = Node('head', None)
        self.head.next_node = self.head
        self.length = 0

    def append(self, data):
        # 在队尾插入数据
        if self.length == 0:
            self.head.data = data
            self.length = 1
            return
        tmp = self.head
        while tmp.next_node != self.head:
            tmp = tmp.next_node
        node = Node(data, None)
        tmp.next_node = node
        node.next_node = self.head
        self.length += 1

    def remove(self, node, pre_node):
        # 删除node
        if self.length == 0:
            return
        if self.length == 1:
            self.head = None
            self.tail = self.head
            return
        pre_node.next_node = node.next_node
        del node
        self.length -= 1

    def travel(self):
        node = self.head.next_node
        for i in range(self.length-1):
            print node.data
            node = node.next_node

    def get_length(self):
        return self.length

    def josephus(self, m):
        # 每m步删除一个元素
        if self.get_length() == 0:
            print 'length = 0'
            return None
        if self.get_length() == 1:
            print 'length = 1'
            return self.head.next_node
        current_node = self.head
        pre_current_node = None
        while self.get_length() >= 2:
            for i in range(m-1):
                pre_current_node = current_node
                current_node = current_node.next_node
            del_node = current_node
            current_node = current_node.next_node
            print 'remove data :', del_node.data
            self.remove(del_node, pre_current_node)
        return self.head.next_node


if __name__ == '__main__':
    cll = CircularLinkList()
    all_data = range(10)
    for data in all_data:
        cll.append(data)
    cll.travel()
    print 'length :', cll.get_length()

    print 'josephus :', cll.josephus(3).data



