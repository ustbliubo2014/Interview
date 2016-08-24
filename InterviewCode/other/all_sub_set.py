# encoding: utf-8
__author__ = 'liubo'

"""
@version: 
@author: 刘博
@license: Apache Licence 
@contact: ustb_liubo@qq.com
@software: PyCharm
@file: all_sub_set.py [找出序列所有子集]
@time: 2016/6/13 22:29
"""


def find_one_sub_list(all_input_dic, prefix):
    '''
    :param all_input_dic: {t1:0,t2:1,t3:2,t4:3,t5:4}
    :param prefix: t1t3
    :return:[t4t5] -- prefix增序
    '''
    return all_input_dic.get(prefix[-1]) + 1


def add_to_prefix(result, prefix, sub_list):
    for index, element in enumerate(sub_list):
        result.append(prefix+element)


def find_all_sub_set(input_list):
    all_input_dic = dict(zip(input_list, range(len(input_list))))
    result = ['']
    all_sub_list = [input_list]
    start = 0
    while len(all_sub_list) > 0:
        for index in range(start, len(result)):
            add_to_prefix(result, result[index], all_sub_list[index-start])
        start += len(all_sub_list)
        all_sub_list = []
        for index in range(start, len(result)):
            all_sub_list.append(input_list[find_one_sub_list(all_input_dic, result[index]):])
    return result[1:]


if __name__ == '__main__':
    input_list = ['a', 'b', 'c', 'd']
    print find_all_sub_set(input_list)