#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:44:24 2019

@author: mkbhanu
"""

import re

def Main():
    stanza = "Two roads diverged in a wood, and I took the one less traveled by, and that has made all the difference."
    
    matchResult = re.match('wood', stanza, re.M | re.I)
    if matchResult:
        print("Match found: " + matchResult.group())
    else:
        print("No match was found")
        
    searchResult = re.search('wood', stanza, re.M | re.I)
    if searchResult:
        print("Search found: " + searchResult.group())
    else:
        print("No search results")
        
if __name__ == "__main__":
    Main()