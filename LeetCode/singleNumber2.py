# encoding: utf-8

"""
@author: liubo-it
@software: PyCharm Community Edition
@file: singleNumber2.py
@time: 2016/8/25 18:23
@contact: ustb_liubo@qq.com
@annotation: singleNumber2
    所有数字异或,找到哪位不一样,然后分成两组,在分别异或
"""
import sys
import logging
from logging.config import fileConfig
import os
import math

reload(sys)
sys.setdefaultencoding("utf-8")
fileConfig('logger_config.ini')
logger_error = logging.getLogger('errorhandler')


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        init = reduce(lambda x, y: x^y, nums, 0)
        if init > 0:
            k = int(math.log(init, 2))
            tmp1 = tmp2 = 0
            for num in nums:
                if ((num >> k) & 1) == 0:
                    tmp1 ^= num
                else:
                    tmp2 ^= num
            return tmp1, tmp2
        else:
            # 有一个是负数,直接按正负来分
            tmp1 = tmp2 = 0
            for num in nums:
                if num >= 0:
                    tmp1 ^= num
                else:
                    tmp2 ^= num
            return tmp1, tmp2


if __name__ == '__main__':
    solution = Solution()
    nums = [43772400,1674008457,1779561093,744132272,1674008457,448610617,1779561093,124075538,
            -1034600064,49040018,612881857,390719949,-359290212,-812493625,124732,-1361696369,
            49040018,-145417756,-812493625,2078552599,1568689850,865876872,865876872,-1471385435,
            1816352571,1793963758,2078552599,-1034600064,1475115274,-119634980,124732,661111294,-1813882010,
            1568689850,448610617,1347212898,-1293494866,612881857,661111294,-1361696369,1816352571,-1813882010,
            -359290212,1475115274,1793963758,1347212898,43772400,-1471385435,124075538,-1293494866,-119634980,390719949]
    print solution.singleNumber(nums)
