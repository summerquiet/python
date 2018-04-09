#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

'''
This is a decryption for krypton4
Decrypt table
NFDXEN
'''

import sys

# Decrypt table
Decypt_table = [4, 6, 19, 24, 5, 13]

Alphabet_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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

    #print(string)

    # Create the alphabet dictionary
    alphabet_dict = dict()
    for index in range(0, len(Alphabet_table)):
        alphabet_dict[Alphabet_table[index]] = index

    # Create the revers dictionary
    revers_dict = dict()
    for key in alphabet_dict:
        revers_dict[alphabet_dict[key]] = key


    str_out = str()
    for i in range(0, len(string)):
        if i % 6 == 4:
            str_out += string[i]

    print(str_out)

'''
    # Decrypt
    str_out = str()
    for i in range(0, len(string)):
        tmp_cnt = alphabet_dict[string[i]] + Decypt_table[i%6]
        tmp_cnt = tmp_cnt % 26
        str_out += revers_dict[tmp_cnt]
'''


if __name__ == '__main__':
    main()

#EOF
