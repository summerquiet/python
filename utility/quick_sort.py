#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
Quick Sort
'''

import copy
import random
import time
import numpy as np


__MAX_DEEP_LEVEL = 50


def quick_sort(sort_list):
    '''
    qucik sort function\n
    input sort_list\n
    output ret_list\n
    '''
    #ret_list = copy.deepcopy(sort_list)
    ret_list = sort_list

    # quick sort list from 0 to length and level is 0
    __quick_sort(ret_list, 0, len(ret_list) - 1)
    return ret_list


def __quick_sort(sort_list, begin, end):
    '''quick sort working function'''
    # end the function
    if begin >= end:
        return sort_list

    # find item position
    pos = __find_pos(sort_list, begin, end)

    # recursive
    __quick_sort(sort_list, begin, pos - 1)
    __quick_sort(sort_list, pos + 1, end)
    return sort_list


def __find_pos(sort_list, begin, end):
    '''find item position in the list'''
    # select more random key in list
    if end - begin > 2:
        __select_key(sort_list, begin, end)

    # find key postion
    i = begin
    j = end
    key = sort_list[begin]

    while i < j:
        while i < j and key <= sort_list[j]:
            j -= 1
        sort_list[i] = sort_list[j]
        while i < j and sort_list[i] <= key:
            i += 1
        sort_list[j] = sort_list[i]
    sort_list[i] = key

    return i


def __select_key(sort_list, begin, end):
    '''
    select key for more random
    get 3 random items from list in [begin:end]
    get middle value one and switch with list[begin]
    '''
    random1 = random.randint(begin, end)
    random2 = random.randint(begin, end)
    random3 = random.randint(begin, end)

    # get mid one
    mid = random1
    if random1 < random2 and random1 < random3:
        if random2 < random3:
            mid = random2
        else:
            mid = random3
    elif random1 < random2 and random1 >= random3:
        mid = random1
    elif random1 >= random2 and random1 < random3:
        mid = random1
    else:
        if random2 < random3:
            mid = random3
        else:
            mid = random2

    # switch value with begin
    tmp = sort_list[begin]
    sort_list[begin] = sort_list[mid]
    sort_list[mid] = tmp


def main():
    '''main function'''
    test_list = np.random.random_integers(1, 100, size=1000)
    test_list = quick_sort(test_list)

    try:
        time_start = time.perf_counter()

        ret = quick_sort(test_list)

        time_end = time.perf_counter()

        print(ret)
        print(time_start, time_end, time_end - time_start)
    except RecursionError as e_arg:
        print(e_arg)


if __name__ == '__main__':
    main()

#EOF
