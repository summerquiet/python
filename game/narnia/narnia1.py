#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

'''
This is a analysis program for narnia1
'''

'''
#include <stdio.h>

int main(){
	int (*ret)();

	if(getenv("EGG")==NULL){    
		printf("Give me something to execute at the env-variable EGG\n");
		exit(1);
	}

	printf("Trying to execute EGG!\n");
	ret = getenv("EGG");
	ret();

	return 0;
}
'''

import sys
import os

def main():

    ret = os.getenv("EGG")
    print(ret)

    return


if __name__ == '__main__':
    main()

#EOF
