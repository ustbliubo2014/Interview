# encoding: utf-8

"""
@author: liubo-it
@software: PyCharm Community Edition
@file: tmp.py
@time: 2016/8/9 11:13
@contact: ustb_liubo@qq.com
@annotation: tmp
"""
import sys
import logging
from logging.config import fileConfig
import os

# reload(sys)
# sys.setdefaultencoding("utf-8")
# fileConfig('logger_config.ini')
# logger_error = logging.getLogger('errorhandler')
from copy import deepcopy

def exchange(lis):
    tmp = deepcopy(lis[3])
    # lis[3] = deepcopy(lis[5])
    # lis[5] = deepcopy(tmp)
    # lis[5] = 3
    # lis[3] = 5
    lis[3], lis[5] = lis[5], lis[3]


lis = range(10)
print lis
exchange(lis[:])
print lis
