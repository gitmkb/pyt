#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 18:01:10 2019

@author: mkbhanu
"""

import argparse

def fibo(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('num', help='Number for which to calculate \
                        Fibonacci number', type=int)
    parser.add_argument('-o', '--output', help='Output result to a file', \
                        action='store_true')
    args = parser.parse_args()
    
    result = fibo(args.num)
    print('The ' + str(args.num) + 'th fib number is ' + str(result))
    
    if args.output:
        f = open('fibonacci.txt', 'a')
        f.write('Fibonacci number is: ' + str(result) + '\n')
    
    
if __name__ == '__main__':
    Main()
#     x = input('x: ')
#     print(fibo(int(x)))
