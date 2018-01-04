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

    return

def __quick_sort(sort_list, begin, end):
    '''
    '''
    if (begin >= end):
        return

    # calcualte a new pos
    pos = __calc(sort_list, begin, end)

    # recursive
    __quick_sort(sort_list, begin, pos - 1)
    __quick_sort(sort_list, pos + 1, end)

def __calc(sort_list, begin, end):
    '''
    '''
    return (begin + end) / 2


def main():
    '''main function'''
    test_list = np.random.random_integers(1, 100, 100)
    print(test_list)

    quick_sort(test_list)
    print(test_list)

if __name__ == '__main__':
    main()

#EOF
