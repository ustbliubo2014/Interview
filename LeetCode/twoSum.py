# encoding: utf-8

"""
@author: liubo-it
@software: PyCharm Community Edition
@file: twoSum.py
@time: 2016/8/25 18:13
@contact: ustb_liubo@qq.com
@annotation: twoSum
    将所有元素存成dict, 利用查找来做
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
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers_dict = dict(zip(nums, range(len(nums))))
        for index, element in enumerate(nums):
            need_num = target - element
            if need_num in numbers_dict:
                other_index = numbers_dict.get(need_num)
                if other_index == index:
                    continue
                else:
                    return index, numbers_dict.get(need_num)


if __name__ == '__main__':
    nums = [3, 2, 4]
    solution = Solution()
    print solution.twoSum(nums, 6)
