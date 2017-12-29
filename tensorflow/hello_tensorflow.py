#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

'''
This is a hello tensorflow script
for test tensorflow installed successfully
'''

import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def main():
    '''main function'''
    hello = tf.constant('Hello, TensorFlow!')
    sess = tf.Session()
    out_str = str(sess.run(hello), encoding='utf-8')
    print(out_str)

if __name__ == '__main__':
    main()

#EOF
