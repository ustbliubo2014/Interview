# encoding: utf-8

"""
@author: liubo
@software: PyCharm
@file: full_permutation.py
@time: 2017/2/28 18:33
@contact: ustb_liubo@qq.com
@annotation: full_permutation
"""
import sys
import logging
from logging.config import fileConfig
import os

reload(sys)
sys.setdefaultencoding("utf-8")
# fileConfig('logger_config.ini')
# logger_error = logging.getLogger('errorhandler')


def full_perumtation(result, str, list):
    if len(list) == 1:
        result.append(str + ',' + list[0])
    else:
        for tmp_str in list:
            tmp_list = list[:]
            tmp_list.remove(tmp_str)
            full_perumtation(result, str + ',' + tmp_str, tmp_list)


if __name__ == '__main__':
    lis = ['a', 'b', 'c', 'd']
    result = []
    str = ''
    full_perumtation(result, str, lis)
    print result