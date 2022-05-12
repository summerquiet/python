#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
Bilibli python agorithm learning P29
'''

'''
topk问题的时间复杂度
1. 先排序再切片，使用快排 O(nlogn)
2. 使用冒泡，选择，插入排序，只对k个数字进行操作 O(nk)
3. 使用堆排序的思路，先建立k大小的堆 O(nlogk)
'''

import random
from cal_time import *

def sift(li:list, low:int, high:int):
    '''
    向下调整, 简历小根堆
    '''
    i = low             # 指向堆的最顶端
    j = 2 * i + 1       # 指向最顶端的子节点
    tmp = li[low]
    while j <= high:
        if j + 1 <= high and li[j + 1] < li[j]:
            j += 1
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
    li[i] = tmp

def heap_topk(li:list, k:int):
    '''
    使用堆排序的方法解决top k的问题
    取list中最大的k个元素
    '''
    heap = li[0:k]
    # 1. 建堆
    for i in range((k - 2 // 2), -1, -1):
        sift(li, i, k -1)
    # 2. 遍历剩余的元素
    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k -1)
    # 3. 出数，将最大的数字放到最后
    for i in range(k - 1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    return heap


# test
li = [random.randint(0, 10000) for i in range(10000)]
print(heap_topk(li, 10))
