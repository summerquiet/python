#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
Quick Sort
'''

import numpy as np

def quick_sort(sort_list):
    '''
    qucik sort function
    input and output all sort_list
    '''
    # quick sort list from 0 to length
    __quick_sort(sort_list, 0, len(sort_list) - 1)
    return sort_list

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

def main():
    '''main function'''
    test_list = np.random.random_integers(1, 100, size=100)
    print(test_list)

    ret = quick_sort(test_list)
    print(ret)

if __name__ == '__main__':
    main()

#EOF
