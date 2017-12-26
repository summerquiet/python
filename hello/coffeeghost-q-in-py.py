#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# 中文用户一定得先用这行来声明, 同时文件本身也得存储成UTF-8编码!
# Quick Python Script Explanation for Programmers
# 给程序员超快速Py脚本解说

import os

def main():

	print 'Hello World!'

	print "这是Alice\'的问候"
	print '这是Bob\'的问候'

	foo(5, 10)

	print '=' * 10
	print '这将直接执行' + os.getcwd()

	counter = 0
	counter += 1

	food = ['苹果', '杏子', '李子', '梨']
	for i in food:
		print '俺就爱整只' + i

	print '数到10'
	for i in range(10):
		print i

def foo(param1, secondParam):
	res = param1 + secondParam
	print '%s 加 %s 等于 %s' %(param1, secondParam, res)

	if res < 50:
		print '这个'
	elif (res >= 50) and ((param1 == 42) or (secondParam == 24)):
		print '那个'
	else:
		print '嗯...'

	return res		# 这里单行注释

'''这是多
行注释......'''

'''
一般在脚本最后调用函数main(); 而且使用内置的运行脚本名来判定;
当且仅当我们直接运行当前脚本时, __name__才为__main__
这样当脚本被当做模块进行 import 导入时, 并不运行 main()
所以, 一般这里是进行测试代码安置的...
'''
if __name__ == '__main__':
	main();
