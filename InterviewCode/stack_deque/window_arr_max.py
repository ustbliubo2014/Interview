# encoding: utf-8
__author__ = 'liubo'

"""
@version: 
@author: 刘博
@license: Apache Licence 
@contact: ustbliubo@qq.com
@software: PyCharm
@file: window_arr_max.py
@time: 2016/6/9 17:07
"""


def window_arr_max(array, window_length):
    '''
        :param array: 数组
        :param window_length: 窗口长度
        :return:
    '''
    result = []
    max_list = [] # 用于存储当前的window_length个数
    if window_length > len(array):
        print 'para error'
        return None
    for index in range(len(array)):
        current = array[index]
        if len(max_list) == 0:
            max_list.append(current)
        else:
            while len(max_list) > 0:
                if max_list[-1] <= current:
                    max_list.pop()
                else:
                    max_list.append(current)
                    break


if __name__ == '__main__':
    array = [4,3,5,4,3,3,6,7]
    window_length = 3
    print window_arr_max(array, window_length)