#!/usr/bin/python
# _*_ coding: UTF-8 _*_

dict = {'姓名':'Kidd', '年龄':27, '职业':'C++ software develper'}
list = dict.keys();
list.sort()

# print list
for key in list:
    print key, ':', dict.get(key, 'NULL')