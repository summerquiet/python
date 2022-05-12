#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
Bilibli python agorithm learning P40
'''

'''
基数排序
以多个标签为标准进行排序
重点在于排序的方法需要是稳定的（stable）
'''

from cal_time import *
import random
import copy
import math

@cal_time
def radix_sort(li:list):
    '''
    基数排序
    算法复杂度O(kn)
    k是位数，如下所示
    最大值 9->1 99->2 888->3 100000->5
    '''
    max_num = max(li)
    # count:int = math.log10(max_num) + 1
    it = 0
    while 10 ** it < max_num:
        buckets = [[] for _ in range(10)]
        # 分桶
        for val in li:
            digit = (val // 10 ** it) % 10
            buckets[digit].append(val)
        # 写回
        li.clear()
        for bucket in buckets:
            li.extend(bucket)
        it += 1
   

def main():
    # test
    li = [random.randint(0, 10000) for i in range(10000)]
    li3 = copy.deepcopy(li)

    #print(li3)
    radix_sort(li3)
    #print(li3)

if __name__ == '__main__':
    main()
