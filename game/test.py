#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

from morse_code_analysis import MorseCodeAnalysis

case1_str = 'woxiangni'
print(case1_str)
case1_code = MorseCodeAnalysis.string_to_morse_code(case1_str)
print(case1_code)
print(MorseCodeAnalysis.morse_code_to_string(case1_code))

#EOF
