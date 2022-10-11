#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

'''
This is a Frequency Analysis for krypton3
File:
found1
found2
found3
krypton4
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

    print(data)
    
    # Cut string
    string = str(data)
    pattern = re.compile(r'\'.*\'')
    match = pattern.search(string)
    string = match.group()[1:string.__len__() - 4]

    # Frequence Analysis
    match2 = list(string)

    # Create a dictionary
    dict1 = dict()
    for word in match2:
        if dict1.get(word):
            dict1[word] = dict1[word] + 1
        else:
            dict1[word] = 1

    # Output analysis result
    items = sorted(dict1.items(), key=lambda d:d[1], reverse=True)

    for key, value in items:
        print(key, value * 100.0 / len(match2))


if __name__ == '__main__':
    main()

# EOF
