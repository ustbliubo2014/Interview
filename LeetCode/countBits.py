# encoding: utf-8

"""
@author: liubo-it
@software: PyCharm Community Edition
@file: countBits.py
@time: 2016/8/24 19:05
@contact: ustb_liubo@qq.com
@annotation: countBits
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
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """


if __name__ == '__main__':
    pass
