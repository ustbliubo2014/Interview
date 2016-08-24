# encoding: utf-8
__author__ = 'liubo'

"""
@version:
@author: 刘博
@license: Apache Licence
@contact: ustb_liubo@qq.com
@software: PyCharm
@file: maxTree.py
@time: 2016/6/10 9:33
"""


def push_stack(stack, top):
    if len(stack) == 0:
        stack.append(top)
    else:
        t = stack.pop()
        push_stack(stack, top)
        stack.append(t)


def reverseStack(stack):
    if len(stack) > 0:
        top = stack.pop()
        reverseStack(stack)
        push_stack(stack, top)
    pass


class Stack(object):
    def __init__(self):
        self.items = []

    def push(self,data):
        self.items.append(data)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            print 'Stack is empty'
            return None

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        else:
            print 'Stack is empty'
            return None

    def travel(self):
        for k in self.items:
            print k


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.travel()
    reverseStack(stack.items)
    stack.travel()
