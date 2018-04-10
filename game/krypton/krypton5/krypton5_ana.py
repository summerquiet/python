#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

'''
This is a Analysis for krypton5
File:
found1
found2
found3
krypton6
'''

import sys
import re

# Decrypt table
Decypt_table = 'KEYLENGTH'

Alphabet_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():

    #print('Number of arguments:', len(sys.argv))
    #print('They are:', str(sys.argv))

    # Data is standard input
    data = sys.argv[1:]
    if not sys.stdin.isatty():
        data.append(sys.stdin.read())

    #print(data)

    # Get string
    str_in = str()
    for char in str(data):
        if char not in '[\' ]':
            str_in += char

    print (str_in)

    # Create the alphabet dictionary
    alphabet_dict = dict()
    for index in range(0, len(Alphabet_table)):
        alphabet_dict[Alphabet_table[index]] = index

    # Create the revers dictionary
    revers_dict = dict()
    for key in alphabet_dict:
        revers_dict[alphabet_dict[key]] = key

    # Decrypt
    str_out = str()
    for i in range(0, len(str_in)):
        tmp_cnt = alphabet_dict[str_in[i]] - alphabet_dict[Decypt_table[i%len(Decypt_table)]]
        tmp_cnt = tmp_cnt % 26
        str_out += revers_dict[tmp_cnt]

    print(str_out)


if __name__ == '__main__':
    main()

#EOF
