# encoding: utf-8

"""
@author: liubo
@software: PyCharm
@file: test.py
@time: 2017/2/28 18:25
@contact: ustb_liubo@qq.com
@annotation: list_sum : 输入一个正整数数组，将它们连接起来排成一个数，输出能排出的所有数字中最小的一个。
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
    a = [321, 32]
    # a = [32, 321]
    def cmp(x1, x2):
        if int(str(x1) + str(x2)) > int(str(x2) + str(x1)):
            return -1
        else:
            return 1
    a.sort(cmp=cmp)
    print ''.join(map(str, a))
