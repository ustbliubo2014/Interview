# encoding: utf-8

"""
@author: liubo
@software: PyCharm
@file: 非连续最大和.py
@time: 2017/1/20 10:00
@contact: ustb_liubo@qq.com
@annotation: 非连续最大和
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
    L = [1, -1, 5, 9]
    n = len(L)
    f = list(L)
    for i in range(n):
        if i > 0:
            f[i] = max(f[i], f[i - 1])
        if i > 1:
            f[i] = max(f[i], f[i - 2] + L[i])
    print(f[n - 1])

