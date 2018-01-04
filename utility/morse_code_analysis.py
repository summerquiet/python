#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
This is a Morse Code Analysis tool
'''

'''
Morse Code
摩斯电码:
1. 一点的长度是1个单位
2. 一划的长度是3个单位
3. 在一个字母中点划的间隔是1个单位
4. 字母和字母之间的间隔是3个单位
5. 两个单词之间的间隔是7个单位

case1:
string: woxiangni
morse:  *--/---/-**-/**/*-/-*/--*/-*/**
case2:
string: I miss you
morse:  **/ /--/**/***/***/ /-*--/---/**-

Switch table
char    sign    code
A       .-      10111
B       -...    111010101
C       -.-.    11101011101
D       -..     1110101
E       .       1
F       ..-.    101011101
G       --.     111011101
H       ....    1010101
I       ..      101
J       .---    1011101110111
K       -.-     111010111
L       .-..    101110101
M       --      1110111
N       -.      11101
O       ---     11101110111
P       .--.    10111011101
Q       --.-    1110111010111
R       .-.     1011101
S       ...     10101
T       -       111
U       ..-     1010111
V       ...-    101010111
W       .--     101110111
X       -..-    11101010111
Y       -.--    1110101110111
Z       --..    11101110101
1       .----   10111011101110111
2       ..---   101011101110111
3       ...--   1010101110111
4       ....-   10101010111
5       .....   101010101
6       -....   11101010101
7       --...   1110111010101
8       ---..   111011101110101
9       ----.   11101110111011101
0       -----   1110111011101110111
'       /       000
space   space   0
'''

class MorseCodeAnalysis:
    '''
    Morse code analysis class
    support:
    1. string_to_morse_code
    2. morse_code_to_string
    '''

    @classmethod
    def string_to_morse_code(cls, in_string):
        '''Convert string to morse code'''
        return cls.__sign_to_code(cls, cls.__str_to_sign(cls, in_string))

    @classmethod
    def morse_code_to_string(cls, in_code):
        '''Convert morse code to string'''
        return cls.__sign_to_str(cls, cls.__code_to_sign(cls, in_code))

    __CHAR_TO_MORSE_SIGN_TABLE = {
        'A' : '.-',
        'B' : '-...',
        'C' : '-.-.',
        'D' : '-..',
        'E' : '.',
        'F' : '..-.',
        'G' : '--.',
        'H' : '....',
        'I' : '..',
        'J' : '.---',
        'K' : '-.-',
        'L' : '.-..',
        'M' : '--',
        'N' : '-.',
        'O' : '---',
        'P' : '.--.',
        'Q' : '--.-',
        'R' : '.-.',
        'S' : '...',
        'T' : '-',
        'U' : '..-',
        'V' : '...-',
        'W' : '.--',
        'X' : '-..-',
        'Y' : '-.--',
        'Z' : '--..',
        '1' : '.----',
        '2' : '..---',
        '3' : '...--',
        '4' : '....-',
        '5' : '.....',
        '6' : '-....',
        '7' : '--...',
        '8' : '---..',
        '9' : '----.',
        '0' : '-----',
        ' ' : ' '
    }

    __SIGN_TO_MORSE_CODE_TABLE = {
        '.' : '1',
        '-' : '111',
        '/' : '000',
        ' ' : '0',
    }

    def __str_to_sign(self, in_str):
        '''Convert from a string to morse sign'''
        in_upper = in_str.upper()
        step = 0
        out_morse = ''

        while step < len(in_upper) - 1:
            if in_upper[step] in self.__CHAR_TO_MORSE_SIGN_TABLE:
                out_morse += self.__CHAR_TO_MORSE_SIGN_TABLE[in_upper[step]] + '/'
            step += 1

        if step != 0:
            if in_upper[step] in self.__CHAR_TO_MORSE_SIGN_TABLE:
                out_morse += self.__CHAR_TO_MORSE_SIGN_TABLE[in_upper[step]]

        return out_morse

    def __sign_to_code(self, in_sign):
        '''Convert from a morse sign to morse code'''
        sign_table = ['.', '-']
        step = 0
        out_code = ''

        while step < len(in_sign) - 1:
            if in_sign[step] in sign_table and in_sign[step + 1] in sign_table:
                if in_sign[step] in self.__SIGN_TO_MORSE_CODE_TABLE:
                    out_code += self.__SIGN_TO_MORSE_CODE_TABLE[in_sign[step]] + '0'
            else:
                if in_sign[step] in self.__SIGN_TO_MORSE_CODE_TABLE:
                    out_code += self.__SIGN_TO_MORSE_CODE_TABLE[in_sign[step]]
            step += 1

        if step != 0:
            if in_sign[step] in self.__SIGN_TO_MORSE_CODE_TABLE:
                out_code += self.__SIGN_TO_MORSE_CODE_TABLE[in_sign[step]]

        return out_code

    def __code_to_sign(self, in_code):
        '''Analysis morse code to sign'''
        out_sign = ''
        step = 0
        stack = ''

        while step < len(in_code):
            if in_code[step] == '0':
                if stack == '111':
                    out_sign += '-'
                    stack = '0'
                elif stack == '1':
                    out_sign += '.'
                    stack = '0'
                elif stack == '00':
                    out_sign += '/'
                    stack = ''
                elif stack == '' and out_sign[len(out_sign) -1] == '/':
                    out_sign += ' '
                else:
                    stack += in_code[step]
            else:
                if stack == '0':
                    stack = ''

                stack += in_code[step]

            step += 1

        if stack == '111':
            out_sign += '-'
        elif stack == '1':
            out_sign += '.'

        return out_sign

    def __sign_to_str(self, in_sign):
        '''Analysis morse sign to string'''
        out_str = ''
        step = 0

        morse_sign_to_char_table = dict((k, v) \
            for [v, k] in self.__CHAR_TO_MORSE_SIGN_TABLE.items())

        while step < len(in_sign):
            old_step = step
            try:
                step = in_sign.index('/', old_step)
                sub = in_sign[old_step:step]
            except ValueError:
                sub = in_sign[step:]
                step = len(in_sign) - 1

            if sub in morse_sign_to_char_table:
                out_str += morse_sign_to_char_table[sub]

            step += 1

        return out_str
#end class morse_code_analysis:

def main():
    ''' main function for test'''

    case1_str = 'woxiangni'
    print(case1_str)
    case1_code = MorseCodeAnalysis.string_to_morse_code(case1_str)
    print(case1_code)
    print(MorseCodeAnalysis.morse_code_to_string(case1_code))

    case2_str = 'I miss you'
    print(case2_str)
    case2_code = MorseCodeAnalysis.string_to_morse_code(case2_str)
    print(case2_code)
    print(MorseCodeAnalysis.morse_code_to_string(case2_code))

if __name__ == '__main__':
    main()
#EOF
