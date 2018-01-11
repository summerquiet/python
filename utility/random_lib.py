#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
random library
'''

import random


def random_integers(low, high, size):
    '''
    get random integers list
    '''
    ret = []

    for i in range(0, size):
        ret.append(random.randint(low, high))

    return ret


def compare(a, b):
    return a > b

def main():
    '''main function'''
    test_list = random_integers(0, 100, size=100)
    print(test_list)
    print(sorted(test_list, reverse=True))


if __name__ == '__main__':
    main()

#EOF
