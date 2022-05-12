#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
Bilibli python agorithm learning P30
'''

'''
归并排序
'''

from cal_time import *
import random
import copy

def merge(li:list, low:int, mid:int, high:int):
    '''
    一次归并的过程
    '''
    '''
    2 5 7 8 9 1 3 4 6
    ^         ^     ^
    |         |     |
    low       mid   high
    归并完成后
    1 2 3 4 5 6 7 8 9
    '''
    i = low
    j = mid
    ltmp:list = []
    while i <= mid - 1 and j <= high:
        if (li[i] < li[j]):
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    while i <= mid - 1:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high + 1] = ltmp

def _merge_sort(li:list, low:int, high:int):
    '''
    归并排序的递归主体
    '''
    if low < high:
        mid = (low + high) // 2
        _merge_sort(li, low, mid)
        _merge_sort(li, mid + 1, high)
        merge(li, low, mid + 1, high)

@cal_time
def merge_sort(li:list):
    '''
    归并排序
    算法复杂度O(nlogn)
    '''
    _merge_sort(li, 0, len(li) - 1)


# test
li = [random.randint(0, 10000) for i in range(10)]
li4 = copy.deepcopy(li)
print(li4)
merge_sort(li4)
print(li4)
