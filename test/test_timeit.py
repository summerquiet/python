#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys
import timeit
import numpy as np
import time

sys.path.append('..')
from utility import quick_sort

def main():
    '''main function'''

    test_list = np.random.randint(1, 100, size=100)
    print(test_list)

    # quick sort
    time_start = time.perf_counter()
    ret = quick_sort.quick_sort(test_list)
    time_end = time.perf_counter()
    print(test_list, ret)
    print(time_end - time_start)

    # sorted
    time_start = time.perf_counter()
    ret = sorted(test_list)
    time_end = time.perf_counter()
    print(test_list, ret)
    print(time_end - time_start)

    # L.sort
    time_start = time.perf_counter()
    test_list.sort()
    time_end = time.perf_counter()
    print(test_list)
    print(time_end - time_start)


'''
    test_timer = timeit.Timer(
        stmt="quick_sort.quick_sort(TEST_LIST)",
        setup="import sys\nsys.path.append('..')\nfrom utility import quick_sort\nimport numpy as np\nTEST_LIST = np.random.randint(1, 100, size=10000)")
    print(test_timer.repeat(repeat=5, number=1))
'''

if __name__ == '__main__':
    main()

#EOF
