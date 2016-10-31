# encoding: utf-8
__author__ = 'liubo'

"""
@version: 
@author: 刘博
@license: Apache Licence 
@contact: ustb_liubo@qq.com
@software: PyCharm
@file: find_min.py
@time: 2016/10/31 16:06
"""

import logging
import os
import sys


def find_min(lis):
    start = 0
    end = len(lis) - 1
    while start < end:
        if lis[start] > lis[end]:
            mid = (start + end) / 2
            if lis[mid] > lis[start]:
                start = mid
                continue
            elif lis[mid] < lis[end]:
                end = mid
                continue
            if lis[mid] == lis[start]:
                return lis[start+1]
        else:
            return lis[start]
    return lis[mid]



if __name__ == '__main__':
    all_lis = [
        [1,2,3,4,5,6,7,8,9],
        [2,3,4,5,6,7,8,9,1],
        [3,4,5,6,7,8,9,1,2],
        [4,5,6,7,8,9,1,2,3],
        [5,6,7,8,9,1,2,3,4],
        [6,7,8,9,1,2,3,4,5],
        [7,8,9,1,2,3,4,5,6],
        [8,9,1,2,3,4,5,6,7],
        [9,1,2,3,4,5,6,7,8],
    ]
    for lis in all_lis:
        min_value = find_min(lis)
        print min_value