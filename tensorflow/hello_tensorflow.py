#! /usr/bin/env python3.5
# _*_ coding: utf-8 _*_

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

'''
Main function
'''
def main():
    hello = tf.constant('Hello, TensorFlow!')
    sess = tf.Session()
    out_str = str(sess.run(hello), encoding='utf-8')
    print(out_str)

if __name__ == '__main__':
    main()

#EOF
