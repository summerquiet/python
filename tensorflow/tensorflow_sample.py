#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

'''
A sample for tensorflow learning
'''

import tensorflow as tf

def main1():
    '''main function'''
    '''
    创建一个常量 op, 产生一个 1x2 矩阵. 这个 op 被作为一个节点
    加到默认图中.
    构造器的返回值代表该常量 op 的返回值.
    '''
    matrix1 = tf.constant([[3., 3.]])

    '''
    创建另外一个常量 op, 产生一个 2x1 矩阵.
    '''
    matrix2 = tf.constant([[2.], [2.]])

    '''
    创建一个矩阵乘法 matmul op , 把 'matrix1' 和 'matrix2' 作为输入.
    返回值 'product' 代表矩阵乘法的结果.
    '''
    product = tf.matmul(matrix1, matrix2)

    # 启动默认图.
    with tf.Session() as sess:
        '''
        调用 sess 的 'run()' 方法来执行矩阵乘法 op, 传入 'product' 作为该方法的参数.
        上面提到, 'product' 代表了矩阵乘法 op 的输出, 传入它是向方法表明, 我们希望取回
        矩阵乘法 op 的输出.

        整个执行过程是自动化的, 会话负责传递 op 所需的全部输入. op 通常是并发执行的.

        函数调用 'run(product)' 触发了图中三个 op (两个常量 op 和一个矩阵乘法 op) 的执行.

        返回值 'result' 是一个 numpy `ndarray` 对象.
        '''
        result = sess.run([product])
        print(result)

def main2():
    '''main function test 2'''
    sess = tf.InteractiveSession()

    x = tf.Variable([1.0, 2.0])
    a = tf.constant([3.0, 3.0])

    # 使用初始化器 initializer op 的 run() 方法初始化 'x'
    x.initializer.run()

    # 增加一个减法 subtract op, 从 'x' 减去 'a'. 运行减法 op, 输出结果
    sub = tf.subtract(x, a)
    print(sub.eval())


if __name__ == '__main__':
    main2()

#EOF
