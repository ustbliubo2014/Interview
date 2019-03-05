# encoding: utf-8

"""
@author: liubo
@contact: lb136883@mail.alibaba-inc.com
@software: PyCharm Community Edition
@file: merge_sort.py
@time: 2019/2/14 22:45
"""

def merge(list1, list2):
    merge_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merge_list.append(list1[i])
            i += 1
        else:
            merge_list.append(list2[j])
            j += 1
    while i < len(list1):
        merge_list.append(list1[i])
        i += 1
    while j < len(list2):
        merge_list.append(list2[j])
        j += 1
    return merge_list


def merge_sort(data_list):
    if len(data_list) < 2:
        return data_list
    middle = len(data_list) / 2
    left = merge_sort(data_list[:middle])
    right = merge_sort(data_list[middle:])
    return merge(left, right)


if __name__ == '__main__':
    data_list = [49, 38, 65, 97, 76, 13, 27, 49]
    # quick_sort_recursion(data_list, 0, len(data_list)-1)
    data_list = merge_sort(data_list)
    print data_list

