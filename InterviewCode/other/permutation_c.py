# encoding: utf-8
__author__ = 'liubo'

"""
@version: 
@author: 刘博
@license: Apache Licence 
@contact: ustb_liubo@qq.com
@software: PyCharm
@file: permutation_c.py
@time: 2016/6/6 23:02
"""


def perm(list, k, m):
    if k > m:
        for i in range(0,m+1):
            print list[i],
        print ''
    else:
        for i in range(k,m+1):
            list[k],list[i] = list[i], list[k]
            perm(list, k+1, m)
            list[k],list[i] = list[i], list[k]


if __name__ == '__main__':
    list = ['a','b','c','d']
    perm(list, 0, 3)