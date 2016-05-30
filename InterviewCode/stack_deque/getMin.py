# encoding: utf-8
__author__ = 'liubo'

"""
@version: 
@author: 刘博
@license: Apache Licence 
@contact: ustb_liubo@qq.com
@site: http://www.phpgao.com
@software: PyCharm
@file: getMin.py
@time: 2016/5/29 22:48
"""


class MinStack():
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def append(self, data):
        if len(self.min_stack) == 0:
            self.min_stack.append(data)
        elif data < self.min_stack[-1]:
            self.min_stack.append(data)
        self.stack.append(data)

    def pop(self):
        data = self.stack.pop()
        if data == self.min_stack[-1]:
            self.min_stack.pop()
        return data

    def getMin(self):
        return self.min_stack[-1]


if __name__ == '__main__':
    minStack = MinStack()
    minStack.append(3)
    print minStack.getMin()
    minStack.append(4)
    print minStack.getMin()
    minStack.append(5)
    print minStack.getMin()
    minStack.append(1)
    print minStack.getMin()
    minStack.append(2)
    print minStack.getMin()
    minStack.pop()
    print minStack.getMin()
    minStack.pop()
    print minStack.getMin()
