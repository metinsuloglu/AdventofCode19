#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 06:23:43 2019

@author: Metin Suloglu
"""

print('~*~*~ Day 4 ~*~*~')

def not_increasing(n):
    num = str(n)
    for i in range(len(num)-1):
        if num[i+1] < num[i]:
            return i, int(num[i])
    return -1

count_one, count_two = 0, 0
i = 125730
while i < 579381:
    decrease_after = not_increasing(i)
    if decrease_after != -1:
        n_update = (5-decrease_after[0])
        pow_update = 10**n_update
        i = (i//pow_update)*pow_update + (int('1'*n_update)*decrease_after[1])
        continue
    n = str(i) # n is non-decreasing
    if any([n.count(c) >= 2 for c in set(n)]):
        count_one += 1
    if any([n.count(c) == 2 for c in set(n)]):
        count_two += 1
    i += 1
    
print('(Part One)')
print(count_one)

print('(Part Two)')
print(count_two)