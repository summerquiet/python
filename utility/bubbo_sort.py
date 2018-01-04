#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
Bubbo Sort
'''

import numpy as np

def bubbo_sort(sort_list):
    '''
    bubbo sort function
    input and output all sort_list
    '''
    length = len(sort_list)

    for i in range(0, length):
        exchange_flag = False
        for j in range(0, length - 1 - i):
            if sort_list[j] > sort_list[j + 1]:
                tmp = sort_list[j]
                sort_list[j] = sort_list[j + 1]
                sort_list[j + 1] = tmp
                exchange_flag = True

        if exchange_flag is False:
            break

    return


def main():
    '''main function'''
    test_list = np.random.random_integers(1, 100, 100)
    print(test_list)

    bubbo_sort(test_list)
    print(test_list)

if __name__ == '__main__':
    main()

#EOF
