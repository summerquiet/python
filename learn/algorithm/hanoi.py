#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
Bilibli python agorithm learning P6
'''

# Hanoi problem recursion function
def hanoi(n, a, b, c):
    if (n > 0):
        hanoi(n - 1, a, c, b)
        print("moving from %s to %s" % (a, c))
        hanoi(n - 1, b, a, c)

hanoi(3, 'A', 'B', 'C')
