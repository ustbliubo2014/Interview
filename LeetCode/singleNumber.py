# encoding: utf-8

"""
@author: liubo-it
@software: PyCharm Community Edition
@file: singleNumber.py
@time: 2016/8/25 17:57
@contact: ustb_liubo@qq.com
@annotation: singleNumber
    所有数字异或
"""
import sys
import logging
from logging.config import fileConfig
import os

reload(sys)
sys.setdefaultencoding("utf-8")
fileConfig('logger_config.ini')
logger_error = logging.getLogger('errorhandler')


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums, 0)


if __name__ == '__main__':
    pass
