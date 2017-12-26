#!/usr/bin/python
# _*_ coding: UTF-8 _*_

a = 3
b = 10

print "a =", a ,", b =", b

#幂
print "a**b =", a**b

#求商的整数部分
print "b//a =", b//a

b1 = False
b2 = True

#and
print "b1 and b2 =", b1 and b2


list = [2,4,6,8,10]

print "list:", list
if (a in list):
    print "a is in the list"
else:
    print "a is not in the list"
if (b in list):
    print "b is in the list"
else:
    print "b is not in the list"

# for loop
fruits = ['banana', 'apple', 'mango', 'grape']
for fruit in fruits:
   print '当前字母 :', fruit

#输出偶数
print '输出偶数'
for index in range(2, 10):
    if (0 == (index % 2)):
        print index

