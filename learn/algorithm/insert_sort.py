#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
Bilibli python agorithm learning P13
'''

from cal_time import *
import random
import copy

@cal_time
def insert_sort(li):
    '''
    插入排序
    算法复杂度O(n^2)
    '''
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1
        while j>= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp

def main():
    # test
    li = [random.randint(0, 10000) for i in range(10000)]

    li3 = copy.deepcopy(li)
    insert_sort(li3)

if __name__ == '__main__':
    main()
