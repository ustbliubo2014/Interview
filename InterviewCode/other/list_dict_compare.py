# encoding: utf-8
__author__ = 'liubo'

"""
@version: 
@author: 刘博
@license: Apache Licence 
@contact: ustb_liubo@qq.com
@software: PyCharm
@file: list_dict_compare.py
@time: 2016/6/21 20:58
"""

from time import time
import numpy as np
from random import randint



lis = range(100000)
np.random.shuffle(lis)

def list_find(lis):
    start = time()
    for i in range(1000):
        randint(1000, 100000) in lis
    end = time()
    print end - start

lis_set = set(lis)
dic = dict(zip(lis, range(len(lis))))

list_find(lis)
list_find(lis_set)
list_find(dic)