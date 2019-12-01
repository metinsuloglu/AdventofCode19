#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 08:08:04 2019

@author: Metin Suloglu
"""

print('~*~*~ Day 1 ~*~*~')

print('(Part One)')
nums = open('day1.txt','r').readlines()
sum = 0
for n in nums:
    sum += int(int(n)/3)-2
        
print(sum)

print('(Part Two)')
sum = 0
for n in nums:
    fuel = int(int(n)/3)-2
    while fuel > 0:
        sum += fuel
        fuel = int(fuel/3)-2
        
print(sum)

print('~*~*~*~*~*~*~*~*~')

