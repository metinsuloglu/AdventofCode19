#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 07:32:39 2019

@author: Metin Suloglu
"""

import csv

print('~*~*~ Day 2 ~*~*~')

def intcode(program, noun, verb):
    program[1] = noun
    program[2] = verb
    i = 0
    while i < len(program):
        if program[i] == 1:
            program[program[i+3]] = program[program[i+1]] + program[program[i+2]]
        elif program[i] == 2:
            program[program[i+3]] = program[program[i+1]] * program[program[i+2]]
        elif program[i] == 99:
            break
        else:
            print('Unknown opcode.')
            return -1
        i += 4
        
    return program[0]

with open('day2.csv') as input_:
    memory = [int(n) for n in next(csv.reader(input_))]

print('(Part One)')
print(intcode(memory.copy(), 12, 2))

print('(Part Two)')
goal = 19690720
halt = False
for noun in range(0,100):
    for verb in range(0,100):
        output = intcode(memory.copy(), noun, verb)
        if output == goal:
            print(100 * noun + verb)
            halt = True
            break
        elif output == -1:
            halt = True
            break
    if halt: break
        
        

