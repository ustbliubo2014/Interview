# encoding: utf-8

"""
@author: liubo
@software: PyCharm Community Edition
@file: SummaryRanges.py
@time: 2016/10/10 10:38
@contact: ustb_liubo@qq.com
@annotation: SummaryRanges
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
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        start = 0
        end = start
        result = []
        if len(nums) == 0:
            return []
        for index in range(len(nums)-1):
            if (nums[index+1] - nums[index]) == 1:
                end += 1
            else:
                if end == start:
                    result.append(str(nums[start]))
                else:
                    result.append(str(nums[start])+"->"+str(nums[end]))
                start = index + 1
                end = start
        if end == start:
            result.append(str(nums[start]))
        else:
            result.append(str(nums[start]) + "->" + str(nums[end]))
        return result


if __name__ == '__main__':
    solution = Solution()
    given = [0, 1, 2, 4, 5, 7]
    result = solution.summaryRanges(given)
    print result
