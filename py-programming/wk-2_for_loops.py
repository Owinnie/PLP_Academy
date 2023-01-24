#!/usr/bin/env python
"""
Using for loops to solve problems
"""

num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
# print(len(num_list))
num_list.sort()
count = 0

for i, n in enumerate(num_list):
    if n > 45:
        print(f"Over 45: {n}")
    else:
        if n == 36:
            print(f"Number found at position: {i}")
            break
        else:
            print(f"Under 45: {n}")
    count += 1
print(f"\nCount = {count}")