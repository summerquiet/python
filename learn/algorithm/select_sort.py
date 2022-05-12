#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
Bilibli python agorithm learning P13
'''

from cal_time import *
import random
import copy

@cal_time
def select_sort(li):
    '''
    选择排序
    算法复杂度O(n^2)
    '''
    for i in range(len(li) - 1):
        for j in range(i + 1, len(li)):
            local = i
            if li[local] > li[j]:
                local = j
            if local != i:
                li[local], li[i] = li[i], li[local]


# test
li = [random.randint(0, 10000) for i in range(10000)]
li2 = copy.deepcopy(li)
# print(li2)
select_sort(li2)
# print(li2)
