#!/usr/bin/env python
# encoding: utf-8

"""
@author: liubo-it
@software: PyCharm Community Edition
@file: BinaryTree.py
@time: 2016/5/27 17:55
@annotation: BinaryTree
"""


def func():
    pass


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        if self.root == None:
            return True
        else:
            return False

    def preOrder(self, tree_node):
        if tree_node == None:
            return
        print tree_node.data
        self.preOrder(tree_node.left)
        self.preOrder(tree_node.right)

    def midOrder(self, tree_node):
        if tree_node == None:
            return
        self.midOrder(tree_node.left)
        print tree_node.data
        self.midOrder(tree_node.right)

    def postOrder(self, tree_node):
        if tree_node == None:
            return
        self.postOrder(tree_node.left)
        self.postOrder(tree_node.right)
        print tree_node.data

    def preOrder_NoRecur(self, root):
        # 前序遍历的非递归实现 --- 用栈实现
        stack = []
        stack.append(root)




if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2, n1, None)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5, n3, n4)
    n6 = Node(6, n2, n5)
    n7 = Node(7, n6, None)
    n8 = Node(8)
    root = Node('root', n7, n8)

    bt = BinaryTree(root)
    print 'preOrder......'
    print bt.preOrder(bt.root)
    print 'inOrder......'
    print bt.midOrder(bt.root)
    print 'postOrder.....'
    print bt.postOrder(bt.root)
    print 'preOrder NoRecur'
    bt.preOrder_NoRecur(bt.root)

