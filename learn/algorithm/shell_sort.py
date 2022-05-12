#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
Bilibli python agorithm learning P34
'''

from cal_time import *
import random
import copy

def insert_sort_gap(li:list, gap:int):
    '''
    插入排序 - 有空隙的版本
    算法复杂度O(n^2)
    '''
    for i in range(gap, len(li)):
        tmp = li[i]
        j = i - gap
        while j>= 0 and li[j] > tmp:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp

@cal_time
def shell_sort(li:list):
    '''
    希尔排序
    分组 d -> d/2
    每个分组使用插入排序
    主要目的是为多线程使用
    '''
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2

def main():
    # test
    li = [random.randint(0, 10000) for i in range(10000)]
    li3 = copy.deepcopy(li)

    #print(li3)
    shell_sort(li3)

if __name__ == '__main__':
    main()
