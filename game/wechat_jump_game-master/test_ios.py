#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

'''
This is a test for iOS device
'''

import wda

def pull_screenshot(client):
    '''get screenshot from iOS device'''
    try:
        client.screenshot('autojump.png')
    except:
        print('screenshot error')

def main():
    '''main function'''
    client = wda.Client()
    session = client.session()

    pull_screenshot(client)

if __name__ == '__main__':
    main()

#EOF
