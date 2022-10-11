#!/usr/bin/python
# _*_ coding: UTF-8 _*_
import random;

#0~99之间的随机数
print '0~99之间的随机数, 且不重复输出:'
list = []
for index in range(100):
    num = random.choice(range(100))
    while (num in list):
        num = random.choice(range(100))
    print num
    list += [num]

print 'Finished!'