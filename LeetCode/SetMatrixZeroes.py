# encoding: utf-8

"""
@author: liubo
@software: PyCharm Community Edition
@file: SetMatrixZeroes.py
@time: 2016/10/17 16:17
@contact: ustb_liubo@qq.com
@annotation: SetMatrixZeroes
"""
import sys
import logging
from logging.config import fileConfig
import os
import numpy as np

reload(sys)
sys.setdefaultencoding("utf-8")
# fileConfig('logger_config.ini')
# logger_error = logging.getLogger('errorhandler')


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        row_num = len(matrix)
        column_num = len(matrix[0])
        row = [0] * row_num
        column = [0] * column_num
        for i in range(row_num):
            for j in range(column_num):
                if matrix[i][j] == 0:
                    row[i] = 1
                    column[j] = 1
        for i in range(row_num):
            if row[i] == 1:
                for k in range(column_num):
                    matrix[i][k] = 0
        for j in range(column_num):
            if column[j] == 1:
                for k in range(row_num):
                    matrix[k][j] = 0


if __name__ == '__main__':
    solution = Solution()
    matrix = [[0, 1]]
    solution.setZeroes(matrix)
    print matrix