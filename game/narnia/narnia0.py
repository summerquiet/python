#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

'''
This is a analysis program for narnia0
'''

'''
#include <stdio.h>
#include <stdlib.h>

int main(){
	long val=0x41414141;
	char buf[20];

	printf("Correct val's value from 0x41414141 -> 0xdeadbeef!\n");
	printf("Here is your chance: ");
	scanf("%24s",&buf);

	printf("buf: %s\n",buf);
	printf("val: 0x%08x\n",val);

	if(val==0xdeadbeef){
        setreuid(geteuid(),geteuid());
		system("/bin/sh");
    }
	else {
		printf("WAY OFF!!!!\n");
		exit(1);
	}

	return 0;
}
'''

def main():

    byte = b'\xef\xbe\xad\xde\x82'
    print(byte)
    string = byte.decode('utf8')
    print('a' * 20 + string)
    
    byte2 = bytes(string, 'utf8')
    print(byte2)


if __name__ == '__main__':
    main()

#EOF
