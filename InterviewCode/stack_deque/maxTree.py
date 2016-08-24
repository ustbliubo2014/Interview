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

'''
    数组必须没有重复元素;根节点最大;时间复杂度O(N),空间复杂度O(N)
'''


import pdb


class Node():
    def __init__(self,value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def popStack_setDict(stack, dict):
    pop_node = stack.pop()
    if len(stack) == 0:
        dict[pop_node] = None
    else:
        dict[pop_node] = stack[-1]


def get_left_big_dict(array):
    # left_big_stack保持递减序列
    left_big_stack = []
    left_big_dict = {}
    for index, node in enumerate(array):
        while len(left_big_stack) > 0 and left_big_stack[-1].value < node.value:
            popStack_setDict(left_big_stack, left_big_dict)
        left_big_stack.append(node)
    while len(left_big_stack) > 0:
        popStack_setDict(left_big_stack, left_big_dict)
    return left_big_dict


def get_right_big_dict(array):
    # 从后往前排,递减序列
    right_big_stack = []
    right_big_dict = {}
    for index in range(len(array)-1, -1, -1):
        node = array[index]
        while len(right_big_stack) > 0 and right_big_stack[-1].value < node.value:
            popStack_setDict(right_big_stack, right_big_dict)
        right_big_stack.append(node)
    while len(right_big_stack) > 0:
        popStack_setDict(right_big_stack, right_big_dict)
    return right_big_dict


def build_max_tree(array):
    left_big_dict = get_left_big_dict(array)
    right_big_dict = get_right_big_dict(array)

    for index in range(len(array)):
        current_node = array[index]

        left_node = left_big_dict.get(current_node)
        right_node = right_big_dict.get(current_node)
        if left_node == None and right_node == None:
            head = current_node
        elif left_node == None:
            if right_node.left == None:
                right_node.left = current_node
            else:
                right_node.right = current_node
        elif right_node == None:
            if left_node.left == None:
                left_node.left = current_node
            else:
                left_node.right = current_node
        else:
            if left_node.value < right_node.value:
                parent_node = left_node
            else:
                parent_node = right_node
            if parent_node.left == None:
                parent_node.left = current_node
            else:
                parent_node.right = current_node
    return head


if __name__ == '__main__':
    node1 = Node(3)
    node2 = Node(4)
    node3 = Node(5)
    node4 = Node(1)
    node5 = Node(2)
    array = [node1, node2, node3, node4, node5]
    head = build_max_tree(array)
    print head.value, head.left.left.value, head.right.left.value
