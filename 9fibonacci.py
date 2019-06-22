#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 18:01:10 2019
Add mutually exclusive group to Fibonacci number program
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
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', action='store_true')
    group.add_argument('-q', '--quiet', action='store_true')
    parser.add_argument('num', help='Number for which to calculate \
                        Fibonacci number', type=int)
    parser.add_argument('-o', '--output', help='Output result to a file', \
                        action='store_true')
    args = parser.parse_args()
    
    result = fibo(args.num)
    if args.verbose:
        print('The ' + str(args.num) + 'th fib number is ' + str(result))
    elif args.quiet:
        print(result)
    else:
        print('fib(' + str(args.num) + ') = ' + str(result))
        
    if args.output:
        f = open('fibonacci.txt', 'a')
        f.write('Fibonacci number is: ' + str(result) + '\n')
    
    
if __name__ == '__main__':
    Main()
#     x = input('x: ')
#     print(fibo(int(x)))
