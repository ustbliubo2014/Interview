# encoding: utf-8
__author__ = 'liubo'

"""
@version: 
@author: 刘博
@license: Apache Licence 
@contact: ustbliubo@qq.com
@software: PyCharm
@file: permutation.py
@time: 2016/6/6 22:44
"""


def permutation(result, str, list):
    if len(list) == 1:
        result.append(str + "-" + list[0])
    else:
        for tmp_str in list:
            tmp_list = list[:]
            tmp_list.remove(tmp_str)
            permutation(result, str + "-" + tmp_str, tmp_list)


if __name__ == '__main__':
    test = []
    permutation(test, '', ['a','b','c','d'])
    test.sort()
    print len(test)
