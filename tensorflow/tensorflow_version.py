#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

from __future__ import absolute_import, division, print_function

import os
import matplotlib.pyplot as plt

import tensorflow as tfimport tensorflow as tf
import tensorflow.contrib.eager as tfe

tf.enable_eager_execution()

print("TensorFlow version: {}".format(tf.VERSION))
print("Eager execution: {}".format(tf.executing_eagerly()))

'''
Output:
TensorFlow version: 1.8.0
Eager execution: True
'''

#EOF
