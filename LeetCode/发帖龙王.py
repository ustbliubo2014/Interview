# encoding: utf-8

"""
@author: liubo
@software: PyCharm
@file: 发帖龙王.py
@time: 2017/2/28 18:48
@contact: ustb_liubo@qq.com
@annotation: 发帖龙王
"""
import sys
import logging
from logging.config import fileConfig
import os

reload(sys)
sys.setdefaultencoding("utf-8")
# fileConfig('logger_config.ini')
# logger_error = logging.getLogger('errorhandler')


if __name__ == '__main__':
    a = [1,2,3,1,1,2,3,1,1,2,1,1,1,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,4]
    count = 0
    x = a[0]
    for index in range(1, len(a)):
        if count == 0:
            x = a[index]
            count += 1
        elif x == a[index]:
            count += 1
        else:
            count -= 1
    print x
