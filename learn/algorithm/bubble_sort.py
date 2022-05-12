#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
Bilibli python agorithm learning P13
'''

import random
from cal_time import *
import copy

@cal_time
def bubble_sort(li):
    '''
    冒泡排序
    算法复杂度O(n^2)
    '''
    for i in range(len(li) - 1):
        flag = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                flag = True
        if not flag:
            return

# test
li = [random.randint(0, 10000) for i in range(10000)]

li1 = copy.deepcopy(li)
bubble_sort(li1)
