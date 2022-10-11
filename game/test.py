#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

from morse_code_analysis import MorseCodeAnalysis

from numpy import array
import knn_sample as knn

def main():
    '''main function'''
    #Test morse_code_analysis
    case1_str = 'woxiangni'
    print(case1_str)
    case1_code = MorseCodeAnalysis.string_to_morse_code(case1_str)
    print(case1_code)
    print(MorseCodeAnalysis.morse_code_to_string(case1_code))

    #Test knn_sample
    data_set, labels = knn.create_data_set()
    in_arr = array([1.1, 0.3])
    k = 3
    out_arr = knn.classify(in_arr, data_set, labels, k)
    print("测试数据为:", in_arr, "分类结果为：", out_arr)

if __name__ == '__main__':
    main()

#EOF
