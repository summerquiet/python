#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

'''
This is a Analysis for krypton4
File:
found1
found2
krypton5
'''

import sys
import re

def main():

    #print('Number of arguments:', len(sys.argv))
    #print('They are:', str(sys.argv))

    # Data is standard input
    data = sys.argv[1:]
    if not sys.stdin.isatty():
        data.append(sys.stdin.read())

    #print(data)
    str_in = str(data)
    string = str()
    for value in str_in:
        if value not in ['[', ']', ' ', '\'']:
            string += value

    str1 = str()
    for i in range(0, string.__len__()):
        if i % 6 == 5:
            str1 += string[i]

    print(str1)


if __name__ == '__main__':
    main()

#EOF
