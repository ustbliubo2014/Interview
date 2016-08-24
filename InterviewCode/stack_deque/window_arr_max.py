# encoding: utf-8
__author__ = 'liubo'

"""
@version: 
@author: 刘博
@license: Apache Licence 
@contact: ustb_liubo@qq.com
@software: PyCharm
@file: window_arr_max.py
@time: 2016/6/9 17:07
"""

from collections import deque


def window_arr_max(array, window_length):
    '''
        :param array: 数组
        :param window_length: 窗口长度
        :return:
    '''
    result = []
    max_list = deque() # 用于存储当前的window_length个数
    max_index_list = deque() # 用于存储对应数字的index,根据index判断是否需要将该数字删除

    if window_length > len(array):
        print 'para error'
        return None

    for index in range(window_length):
        current = array[index]
        if len(max_list) == 0:
            max_list.append(current)
            max_index_list.append(index)
        else:
            has_add = False
            while len(max_list) > 0:
                if max_list[-1] <= current:
                    max_list.pop()
                    max_index_list.pop()
                else:
                    max_list.append(current)
                    max_index_list.append(index)
                    has_add = True
                    break
            if not has_add:
                max_list.append(current)
                max_index_list.append(index)

    for index in range(window_length-1, len(array)):
        current = array[index]
        if len(max_list) == 0:
            max_list.append(current)
            max_index_list.append(index)
        else:
            has_add = False
            while len(max_list) > 0:
                if max_list[-1] <= current:
                    max_list.pop()
                    max_index_list.pop()
                else:
                    max_list.append(current)
                    max_index_list.append(index)
                    has_add = True
                    break
            if not has_add:
                max_list.append(current)
                max_index_list.append(index)
        print 'current :', current,  'index :', index, 'max_index_list :', max_index_list, 'max_list :', max_list
        if index - max_index_list[0] >= window_length:
            max_index_list.popleft()
            max_list.popleft()
        result.append(max_list[0])
    return result


if __name__ == '__main__':
    array = [4,3,5,4,3,5,8,3,6,3,6,7]
    window_length = 3
    print window_arr_max(array, window_length)