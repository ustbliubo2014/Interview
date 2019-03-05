# encoding: utf-8

"""
@author: liubo
@contact: lb136883@mail.alibaba-inc.com
@software: PyCharm Community Edition
@file: quick_sort.py
@time: 2019/2/14 21:26
"""


def quick_sort_recursion(data_list, start, end):
    base = data_list[start]
    if start < end:
        i, j = start, end
        while i < j:
            while i < j and data_list[j] >= base:
                j -= 1
            data_list[i] = data_list[j]
            while i < j and data_list[i] <= base:
                i += 1
            data_list[j] = data_list[i]
        data_list[i] = base
        quick_sort_recursion(data_list, start, i-1)
        quick_sort_recursion(data_list, j+1, end)


def partition(data_list, start, end):
    pivot = data_list[start]
    while start < end:
        if start < end and data_list[end] >= pivot:
            end -= 1
        data_list[start] = data_list[end]
        if start < end and data_list[start] <= pivot:
            start += 1
        data_list[end] = data_list[start]
    data_list[start] = pivot
    return start


def quick_sort_not_recursion(data_list):
    if len(data_list) < 2:
        return
    start = 0
    end = len(data_list) - 1
    stack = []
    stack.append(end)
    stack.append(start)
    while stack:
        l = stack.pop()
        r = stack.pop()
        index = partition(data_list, l, r)
        if index > l + 1:
            stack.append(index-1)
            stack.append(l)
        if index < r - 1:
            stack.append(end)
            stack.append(index+1)


if __name__ == '__main__':
    data_list = [49, 38, 65, 97, 76, 13, 27, 49]
    # quick_sort_recursion(data_list, 0, len(data_list)-1)
    quick_sort_not_recursion(data_list)
    print data_list
