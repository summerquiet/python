#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
Bilibli python agorithm learning P15
'''

import time

def cal_time(func):
	def wraper(*args, **kwargs):
		t1 = time.time()
		result = func(*args, **kwargs)
		t2 = time.time()
		print('%s running time %s　second' % (func.__name__, t2 - t1))
		return result
	return wraper

'''
@cal_time
上面的@cal_time的作用就是 f = cal_time(f)
'''