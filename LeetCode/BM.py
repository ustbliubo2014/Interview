# encoding: utf-8

"""
@author: liubo-it
@software: PyCharm Community Edition
@file: BM.py
@time: 2016/9/12 11:53
@contact: ustb_liubo@qq.com
@annotation: BM
"""
import sys
import logging
from logging.config import fileConfig
import os

reload(sys)
sys.setdefaultencoding("utf-8")
fileConfig('logger_config.ini')
logger_error = logging.getLogger('errorhandler')

def search(txt, pat):
    N = len(txt)
    M = len(pat)
    pos = []
    skip = 0
    right = {}
    for j in range(0, M):
        right[pat[j]] = j
    i = 0
    while i <= N - M:
        for j in range(M - 1, -1, -1):
            if pat[j] != txt[i + j]:
                skip = j - right.get(txt[i + j], -1)
                if skip < 1:
                    skip = 1
                break
            if j == 0:
                pos.append(i)
                skip = M
                break
        i += skip
    return pos


def search_v2(txt, pat):
    N = len(txt)
    M = len(pat)
    pos = []
    skip = 0
    right = {}
    for j in range(0, M):
        right[pat[j]] = j
    i = 0
    delta = {}
    while i <= N - M:
        for j in range(M - 1, -1, -1):
            c1 = txt[i + j]
            c2 = pat[j]
            delta[c1] = j
            if c1 != c2:
                skip1 = j - right.get(c1, -1)
                skip2 = delta.get(c2, -1) - j
                skip = max(skip1, skip2)
                if skip < 1:
                    skip = 1
                break
            if j == 0:
                pos.append(i)
                skip = M
                break
        i += skip
    return pos


if __name__ == '__main__':
    txt = 'ABCSAKDDEFKEHHJDDEFKLD'
    pat = 'DDEFK'
    print search(txt, pat)
    print search_v2(txt, pat)
