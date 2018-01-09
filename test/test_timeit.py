#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys
import timeit
import numpy as np

sys.path.append('..')
from utility import quick_sort

TEST_LIST = np.random.randint(1, 1000, size=1000)
print(TEST_LIST)
RET = quick_sort.quick_sort(TEST_LIST)
print(RET)

TEST_TIMER = timeit.Timer(
    stmt="quick_sort.quick_sort(TEST_LIST)",
    setup="import sys\nsys.path.append('..')\nfrom utility import quick_sort\nimport numpy as np\nTEST_LIST = np.random.randint(1, 100, size=10000)")
print(TEST_TIMER.repeat(repeat=5, number=1))

#EOF
