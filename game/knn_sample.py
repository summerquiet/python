#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
A KNN sample
'''

from numpy import *

def create_data_set():
    '''给出训练数据以及对应的类别'''
    group = array([[1.0, 2.0], [1.2, 0.1], [0.1, 1.4], [0.3, 3.5]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify(in_arr, data_set, label, k):
    '''通过KNN进行分类'''
    data_size = data_set.shape[0]

    #计算欧式距离
    in_set = tile(in_arr, (data_size, 1))
    diff_l = in_set - data_set
    sqdiff = diff_l ** 2

    #行向量分别相加，从而得到新的一个行向量
    square_dist = sum(sqdiff, axis=1)
    dist = square_dist ** 0.5

    #对距离进行排序
    #argsort()根据元素的值从大到小对元素进行排序，返回下标
    sorted_dist_index = argsort(dist)

    class_count = {}
    for i in range(k):
        vote_label = label[sorted_dist_index[i]]

        #对选取的K个样本所属的类别个数进行统计
        class_count[vote_label] = class_count.get(vote_label, 0) + 1

    #选取出现的类别次数最多的类别
    max_count = 0
    for key, value in class_count.items():
        if value > max_count:
            max_count = value
            classes = key

    return classes

def main():
    '''main function'''
    data_set, labels = create_data_set()
    in_arr = array([1.1, 0.3])
    k = 3
    out_arr = classify(in_arr, data_set, labels, k)
    print("测试数据为:", in_arr, "分类结果为：", out_arr)

if __name__ == '__main__':
    main()

#EOF
