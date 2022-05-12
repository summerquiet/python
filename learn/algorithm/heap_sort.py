#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
Bilibli python agorithm learning P21
'''

'''
堆：一种特使的完全二叉树
'''

import random
from cal_time import *

def sift(li:list, low:int, high:int):
    '''
    向下调整
    '''
    i = low             # 指向堆的最顶端
    j = 2 * i + 1       # 指向最顶端的子节点
    tmp = li[low]
    while j <= high:
        if j + 1 <= high and li[j + 1] > li[j]:
            j += 1
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
    li[i] = tmp

@cal_time
def heap_sort(li:list):
    '''
    堆排序
    算法复杂度O(nlogn)
    '''
    n = len(li)
    # 1. 建堆
    for i in range((n - 2 // 2), -1, -1):
        sift(li, i, n - 1)
    # 2. 出数，将最大的数字放到最后
    for i in range(n - 1, 0, -1):
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)


# test
li = [random.randint(0, 10000) for i in range(10000)]
#print(li)
heap_sort(li)
#print(li)
