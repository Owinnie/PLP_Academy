#!/usr/bin/env python
"""
Write a Python program to construct the following pattern,
using a nested for loop.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
pat = 5  # longest width of the pattern
for i in range(pat):
    for j in range(i):
        print("* ", end="")
    print("")

for i in range(pat,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
