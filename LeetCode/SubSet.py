# encoding: utf-8

"""
@author: liubo
@software: PyCharm Community Edition
@file: SubSet.py
@time: 2016/10/17 16:37
@contact: ustb_liubo@qq.com
@annotation: SubSet
"""
import sys
import logging
from logging.config import fileConfig
import os

reload(sys)
sys.setdefaultencoding("utf-8")
# fileConfig('logger_config.ini')
# logger_error = logging.getLogger('errorhandler')


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        has_process_dic = {}
        nums.sort()
        has_process_dic[''] = nums[:]
        no_process_list = ['']
        index_dic = dict(zip(nums, range(len(nums))))
        while len(no_process_list) > 0:
            element = no_process_list.pop()
            element_no_process_list = has_process_dic.get(element)
            for k in element_no_process_list:
                this_new_element = element + ' ' + str(k)
                this_new_element_no_process_list = nums[index_dic.get(k)+1:]
                has_process_dic[this_new_element] = this_new_element_no_process_list
                no_process_list.append(this_new_element)
        result = []
        for k in has_process_dic:
            result.append(map(int, k.rstrip().split()))
        return result


if __name__ == '__main__':
    nums = [1, 2, 2]
    solution = Solution()
    result = solution.subsets(nums)
    print result