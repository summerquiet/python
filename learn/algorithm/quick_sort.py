#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
Bilibli python agorithm learning P13
'''

from cal_time import *
import random
import copy
import sys

sys.setrecursionlimit(100000)

def quick_partition(li:list, left:int, right:int):
    '''快速排序的主要运算'''
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left

def _quick_sort(li:list, left:int, right:int):
    '''快速排序-主要执行函数'''
    if left < right:    # 至少2个元素
        mid = quick_partition(li, left, right)
        _quick_sort(li, left, mid - 1)
        _quick_sort(li, mid + 1, right)

@cal_time
def quick_sort(li:list):
    '''
    快速排序
    算法复杂度O(nlogn)
    '''
    _quick_sort(li, 0, len(li) - 1)


# test
li = [random.randint(0, 10000) for i in range(10000)]

li4 = copy.deepcopy(li)
quick_sort(li4)
