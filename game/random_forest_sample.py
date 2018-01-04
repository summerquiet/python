#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
This is a python sample for Random Forest
Random Foreest: a machine learning classifier
'''

import numpy
import pylab

def main():
    '''main function'''

    x = numpy.random.uniform(1, 100, 1000)
    y = numpy.log(x) + numpy.random.normal(0, .3, 1000)

    pylab.scatter(x, y, s=1, label='log(x) with noise')

    pylab.plot(numpy.arange(1, 100), numpy.log(numpy.arange(1, 100)), c='r', label='log(x) true function')
    pylab.xlabel('x')
    pylab.ylabel('f(x) = log(x)')
    pylab.legend(loc='best')
    pylab.title('A Basic Log Function')
    pylab.show()

if __name__ == '__main__':
    main()

#EOF
