# encoding: utf-8

"""
@author: liubo-it
@software: PyCharm Community Edition
@file: removeElement.py
@time: 2016/8/25 15:08
@contact: ustb_liubo@qq.com
@annotation: removeElement
    类似于快速排序的算法
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
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1
        if len(nums) == 0:
            return 0
        exchange = False
        while i < j:
            while i < j:
                if nums[i] != val:
                    i += 1
                else:
                    break
            while i < j:
                if nums[j] == val:
                    j -= 1
                else:
                    break
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
                exchange = True
        if exchange:
            new_length = j
            nums = nums[:new_length]
            return new_length
        else:
            if nums[i] == val:
                return i
            else:
                return len(nums)


if __name__ == '__main__':
    nums = []
    vals = 3
    solution = Solution()
    print solution.removeElement(nums, vals)
