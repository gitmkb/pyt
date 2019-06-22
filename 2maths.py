#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:31:50 2019

@author: mkbhanu
"""
import sys
import math

x = 0b10                #binary
print(x, bin(x))

x = 0x12c            #hexadecimal
print(x, hex(x))

x = 1 + 2j            #complex number
print(x)

x = 10 / 3          #floating point division
print(x)

x = 10 // 3         #integer division
print(x)

x = 10 % 3          #modulus division
print(x)

x = 10 ** 3         #exponent
print(x)

x += 1              #increment (no x++ / x--)
print(x)

PI = 3.14           #No consts in python
print(round(PI))

z = -10 
print(abs(z))

print(math.floor(PI))
print('Digits: ', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, sep=' ', file=sys.stdout, end='\n', flush=False)
print('Vowels: ', 'a', 'e', 'i', 'o', 'u', sep=' ', end='\n', file=sys.stdout, flush=False)

