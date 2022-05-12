#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
Bilibli python agorithm learning P7
'''

def linear_search(list, value):
    for index, v in enumerate(list):
        if v == value:
            return index
    return None

def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:            # 候选区有值
        mid = (left + right) // 2   # 整除
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    return None

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(li, 10))
