# encoding: utf-8
__author__ = 'liubo'

"""
@version: 
@author: 刘博
@license: Apache Licence 
@contact: ustb_liubo@qq.com
@software: PyCharm
@file: SubSet2.py
@time: 2016/10/17 23:38
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


    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # mapping_relation = dict(zip(map(str, range(len(nums))), map(str, nums)))
        if len(nums) == len(set(nums)):
            return self.subsets(nums)
        max_num = max(nums) + 1
        mapping_relation = {}
        nums.sort()
        tmp_set = set()
        for index, element in enumerate(nums):
            if element in tmp_set:
                mapping_relation[str(max_num)] = str(element)
                max_num += 1
            else:
                mapping_relation[str(element)] = str(element)
            tmp_set.add(element)
        nums = mapping_relation.keys()
        for k in nums:
            if int(k) in tmp_set:
                mapping_relation.pop(k)
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
        result = set()
        mapping_relation_list = mapping_relation.keys()
        mapping_relation_list.sort(reverse=True)
        for k in has_process_dic:
            for m in mapping_relation_list:
                k = k.replace(m, mapping_relation.get(m))
            k = map(int, k.rstrip().split())
            k.sort()
            k = ' '.join(map(str, k))
            result.add(k)
        new_result = []
        for k in result:
            new_result.append(map(int, k.rstrip().split()))
        return new_result


if __name__ == '__main__':
    nums = [-1, 1, 2]
    solution = Solution()
    result = solution.subsetsWithDup(nums)
    print result
