# encoding: utf-8

"""
@author: liubo
@contact: lb136883@mail.alibaba-inc.com
@software: PyCharm Community Edition
@file: max_length_substr.py
@time: 2019/3/4 15:58
"""

import numpy as np


def find_max_length_substr(str1, str2):
    length1 = len(str1)
    length2 = len(str2)
    if length1 == 0 or length2 == 0:
        return -1
    c = [[0 for i in range(length1+1)] for j in range(length2+1)]

    for i in range(1, length1):
        for j in range(1, length2):
            print(i, j, str1[i-1] == str2[j-1])
            if str1[i-1] == str2[j-1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    c = np.asarray(c)
    return c


if __name__ == '__main__':
    max_length = find_max_length_substr('abdfg','abcdfg')
    print(max_length)