#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 07:32:39 2019

@author: Metin Suloglu
"""

from intcode import IntCode

print('~*~*~ Day 2 ~*~*~')

memory = IntCode.read_memory('day2.csv')

print('(Part One)')
print(IntCode(memory.copy(), mem_vals={1:12, 2:2}).run()[0])

print('(Part Two)')
goal = 19690720
halt = False
for noun in range(0,100):
    for verb in range(0,100):
        output = IntCode(memory.copy(), mem_vals={1:noun, 2:verb}).run()[0]
        if output == goal:
            print(100 * noun + verb)
            halt = True
            break
        elif output == -1:
            halt = True
            break
    if halt: break
        
print('~*~*~*~*~*~*~*~*~')

