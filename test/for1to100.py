#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

'''
This is a very sample example for add from 1 to 100
'''

def add(in_a, in_b):
    '''Add function a and b'''
    return in_a + in_b

def main():
    '''Main function'''
    tmp = 0
    for i in range(0, 100):
        tmp = add(tmp, i + 1)

    print(tmp)

if __name__ == '__main__':
    main()

#EOF
