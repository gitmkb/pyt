#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:26:57 2019

@author: mkbhanu
"""

def hello(name):
    """Print "Hello World" and return none"""
    print("Hello {}".format(name))
    
# Main program starts here
#hello()

i = "World"
if __name__ == "__main__":
    hello(i)

def demo(x):
    for i in range(5):
        print("i = {}, x = {}".format(i, x))
        x = x + 1
        
demo(0)

"""Python is a dynamically typed language"""
h = 1
print(type(h))
h = "AString"
print(type(h))

"""Variables are immutable"""
x = 1
print(id(x))
x = x + 1
print(id(x))

"""Lists are mutable"""
x = [0, 1, 2, 3]
print(x)
print(id(x))
x.append(4)
print(x)
print(id(x))

course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[:3])
print(course[0:])
print(course[:])
"""String copied to a memory location"""
print(id(course))
print(id(course[0]))
print(course.upper())
print(course.lower())
print(course.strip())
print(course.find("Pro"))
print(course.replace("P", "-"))
print("Programming" in course)
print("Programming" not in course)

# Escape sequences
message = 'I used to call him "Awesome"!'
print(message)
message = "They used to call him \"Mad\" \\ \"Hopeless\"!"
print(message)
message = "\nThis is first line. \nThis is second line..."
print(message)

first = "Mukesh"
last = "Kumar"
fullname = first + " " + last
print(fullname)

first = "MK"
last = "Bhanu"
fullname = f"{first} {last}"
print(fullname)
full = f"{len(first)} {len(last)}"
print(full)

