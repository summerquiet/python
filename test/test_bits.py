#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

'''
This is a very sample example for test bits operate
'''

def main():

    a = b'101'
    #a = a<<1
    x = int(a, base=2)

    print(bytearray(x))


if __name__ == '__main__':
    main()

#EOF
