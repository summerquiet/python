#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
Bilibli python agorithm learning P38
'''

'''
桶排序
每个桶里放入一定范围的数
'''

from cal_time import *
import random
import copy

@cal_time
def bucket_sort(li:list, n:int=100, max_num:int=10000):
    '''
    桶排序
    默认100个桶，最大的数字范围在10000一下
    '''
    buckets = [[] for _ in range(n)]    # 创建桶
    for val in li:
        i = min(val // (max_num // n), n - 1)
        # 将数字放到对应的桶里
        buckets[i].append(val)
        # 同时对桶内的数字进行排序
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break
    li.clear()
    for bucket in buckets:
        li.extend(bucket)

def main():
    # test
    li = [random.randint(0, 1000) for i in range(10000)]
    li3 = copy.deepcopy(li)

    #print(li3)
    bucket_sort(li3)
    #print(li3)

if __name__ == '__main__':
    main()
