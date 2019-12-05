#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 09:52:50 2019

@author: Metin Suloglu
"""

import csv

print('~*~*~ Day 5 ~*~*~')

opcode_params = {1:3, 2:3, 3:1, 4:1, 5:2, 6:2, 7:3, 8:3, 99:0}

def parse(val):
    modes = []
    rest = val//100
    opcode = val - rest*100
    for i in range(opcode_params[opcode]):
        modes.append(rest % 10)
        rest //= 10
    return opcode, modes

def getVal(program, i, mode):
    return (program[i] if mode == 0 else i)

def intcode(program):
    i = 0
    while i < len(program):
        (opcode, modes) = parse(program[i])
        if opcode == 1:
            program[getVal(program, i+3, modes[2])] = program[getVal(program, i+1, modes[0])] + program[getVal(program, i+2, modes[1])]
        elif opcode == 2:
            program[getVal(program, i+3, modes[2])] = program[getVal(program, i+1, modes[0])] * program[getVal(program, i+2, modes[1])]
        elif opcode == 3:
            program[getVal(program, i+1, modes[0])] = int(input('Input: '))
        elif opcode == 4:
            print(program[getVal(program, i+1, modes[0])])
        elif opcode == 5:
            if program[getVal(program, i+1, modes[0])] != 0:
                i = program[getVal(program, i+2, modes[1])] - opcode_params[opcode] - 1
        elif opcode == 6:
            if program[getVal(program, i+1, modes[0])] == 0:
                i = program[getVal(program, i+2, modes[1])] - opcode_params[opcode] - 1
        elif opcode == 7:
            program[getVal(program, i+3, modes[2])] = int(program[getVal(program, i+1, modes[0])] < program[getVal(program, i+2, modes[1])])
        elif opcode == 8:
            program[getVal(program, i+3, modes[2])] = int(program[getVal(program, i+1, modes[0])] == program[getVal(program, i+2, modes[1])])
        elif opcode == 99:
            break
        else:
            print('Unknown opcode.')
            return -1
        i += opcode_params[opcode] + 1

with open('day5.csv') as input_:
    memory = [int(n) for n in next(csv.reader(input_))]

print('(Part One)')
intcode(memory.copy())

print('(Part Two)')
intcode(memory.copy())