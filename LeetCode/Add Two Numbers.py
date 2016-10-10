# encoding: utf-8

"""
@author: liubo
@software: PyCharm
@file: Add Two Numbers.py
@time: 2016/9/29 19:05
@contact: ustb_liubo@qq.com
@annotation: Add Two Numbers
"""
import sys
import logging
from logging.config import fileConfig
import os

reload(sys)
sys.setdefaultencoding("utf-8")
# fileConfig('logger_config.ini')
# logger_error = logging.getLogger('errorhandler')

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current_node = ListNode(x=0)
        pre_node = current_node
        carry = 0
        while l1.next != None and l2.next != None:
            carry = (l1.val + l2.val + carry) / 10
            current_result = (l1.val + l2.val + carry) % 10
            current_node.val = current_result



if __name__ == '__main__':
    pass
