# encoding: utf-8

"""
@author: liubo-it
@software: PyCharm Community Edition
@file: countNumbersWithUniqueDigits.py
@time: 2016/8/25 12:11
@contact: ustb_liubo@qq.com
@annotation: countNumbersWithUniqueDigits
    利用组合的知识来解决
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
    def factorial(self, last_result, last_factor):
        result = last_result * (last_factor - 1)
        return result, (last_factor - 1)


    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        current_sum = 0
        factor = 10
        result = 1
        for k in range(2, n+1):
            factor -= 1
            result = result * factor
            current_sum += 9 * result
        current_sum += 10
        return current_sum


if __name__ == '__main__':
    solution = Solution()
    print solution.countNumbersWithUniqueDigits(2)
    print solution.countNumbersWithUniqueDigits(3)