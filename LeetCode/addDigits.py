# encoding: utf-8

"""
@author: liubo-it
@software: PyCharm Community Edition
@file: addDigits.py
@time: 2016/8/26 14:41
@contact: ustb_liubo@qq.com
@annotation: addDigits
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
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = str(num)
        while len(result) > 1:
            result = str(reduce(lambda x,y: x+y, map(int,result)))
        return int(result)


if __name__ == '__main__':
    solution = Solution()
    print solution.addDigits(38)
