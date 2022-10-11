#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

'''
This is a decryption for krypton3
Decrypt table
encryption: a   b   c   d   e   f   g   h   i   j   k   l   m
Alphabet:   b   o   i   h   g   k   n   q   v   t   w   y   u

encryption: n   o   p   q   r   s   t   u   v   w   x   y   z
Alphabet:   r   x   z   a   j   e   m   s   l   d   f   p   c
'''

import sys

def main():

    #print('Number of arguments:', len(sys.argv))
    #print('They are:', str(sys.argv))

    # Data is standard input
    data = sys.argv[1:]
    if not sys.stdin.isatty():
        data.append(sys.stdin.read())

    #print(data)
    string = str(data)

    # Create a decryption table dictionary
    decrypt_dict = {
        ' ' : ' ',
        'A' : 'B',
        'B' : 'O',
        'C' : 'I',
        'D' : 'H',
        'E' : 'G',
        'F' : 'K',
        'G' : 'N',
        'H' : 'Q',
        'I' : 'V',
        'J' : 'T',
        'K' : 'W',
        'L' : 'Y',
        'M' : 'U',
        'N' : 'R',
        'O' : 'X',
        'P' : 'Z',
        'Q' : 'A',
        'R' : 'J',
        'S' : 'E',
        'T' : 'M',
        'U' : 'S',
        'V' : 'L',
        'W' : 'D',
        'X' : 'F',
        'Y' : 'P',
        'Z' : 'C'
    }

    str_out = str()
    for letter in string:
        if decrypt_dict.get(letter):
            str_out += decrypt_dict[letter]

    print(str_out)


if __name__ == '__main__':
    main()

#EOF
