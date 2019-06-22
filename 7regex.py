#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:04:59 2019

@author: mkbhanu
"""

import re
import argparse

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('srword', help='Specify your search word')
    parser.add_argument('filename', help='Specify file to search')
    args = parser.parse_args()
    
    searchFile = open(args.filename)
    linenum = 0
    
# When using the same pattern multiple times in a FOR loop, make your program more efficient by compiling the expression. Creating the expression takes the longest time and more cycles on the CPU.
# myRex = re.compile(pattern)
# result = myRex.match(string)
# myRex = re.compile(args.srword)
# res = myRex.match()
  
    for line in searchFile.readlines():
        line = line.strip('\n\r')
        searchResult = re.search(args.srword, line, re.M | re.I)
        linenum += 1
        if searchResult:
            print(str(linenum) + ': ' + line)
            
            
if __name__ == '__main__':
    Main()
