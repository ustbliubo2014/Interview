# encoding: utf-8
__author__ = 'liubo'

"""
@version: 
@author: 刘博
@license: Apache Licence 
@contact: ustb_liubo@qq.com
@software: PyCharm
@file: stack_sort.py
@time: 2016/6/9 16:37
"""


def stack_sort(stack):
    '''
        :param stack: 需要排序的栈
        利用一个辅助栈完成栈的排序
    '''
    pop_num = 0
    stack_tmp = []
    while len(stack) > 0:
        current = stack.pop()
        if len(stack_tmp) == 0:
            stack_tmp.append(current)
        else:
            while current < stack_tmp[-1]:
                stack.append(stack_tmp.pop())
                pop_num += 1
            stack_tmp.append(current)
            for index in range(pop_num):
                stack_tmp.append(stack.pop())
            pop_num = 0
    return stack_tmp


if __name__ == '__main__':
    stack = [1,3,5,7,9,2,4,6,8,0]
    stack = stack_sort(stack)
    print stack