# encoding: utf-8

"""
@author: liubo-it
@software: PyCharm Community Edition
@file: topKFrequent.py
@time: 2016/8/8 15:22
@contact: ustb_liubo@qq.com
@annotation: topKFrequent
"""
import sys
import logging
from logging.config import fileConfig
import os
import numpy as np
import pdb
from copy import deepcopy
import random

class Solution(object):
    def partation(self, nums, pivot):
        '''
            以pivot将数组nums分成两部分(大于pivot的和小于pivot的)
        '''
        i = 0
        length = len(nums)
        j = length - 1
        while i < j:
            while i < j and nums[i] < pivot:
                i += 1
            while j > i and nums[j] > pivot:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums, i

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k < 1 or k > len(nums):
            return None
        topKElement = []
        start = 0
        end = len(nums)
        pivot = nums[random.randint(start, end-1)]
        current_length = 0
        while True:
            new_nums, pivot_index = self.partation(nums[start:end], pivot)
            this_length = end - pivot_index
            nums[start:end] = new_nums[:]
            if current_length + this_length == k:
                topKElement.extend(nums[pivot_index:])
                break
            elif current_length + this_length < k:    # 数量还不足
                topKElement.extend(nums[pivot_index:])
                current_length += this_length
                end = pivot_index
                pivot = nums[start]
                continue
            else:    # 加上后数量超过
                # 在num[pivot_index:end]里找前(k-current_length)个
                element = self.topKFrequent(nums[pivot_index:end], k-current_length)
                topKElement.extend(element)
                break
        return topKElement


if __name__ == '__main__':
    solution = Solution()
    for index in range(100):
        nums = range(30)
        np.random.shuffle(nums)
        find = solution.topKFrequent(nums, 12)
        print np.min(find), np.max(find)

