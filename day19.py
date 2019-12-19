#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 07:49:38 2019

@author: Metin Suloglu
"""

from intcode import IntCode

print('~*~*~ Day 19 ~*~*~')

memory = IntCode.read_memory('day19.csv')

count = 0
for y in range(0, 50):
    for x in range(0, 50):
        _, outputs, _ = IntCode(memory.copy()).run(inputs=[x,y], capture_output=True)
        count += (outputs[-1] == 1)

print('(Part One)')
print(count)

begin_x, y = 0, 99
box_fit = False
while True:
    x = begin_x
    while True:
        _, outputs, _ = IntCode(memory.copy()).run(inputs=[x,y], capture_output=True)
        if outputs[-1] == 1:
            begin_x = x
            _, outputs, _ = IntCode(memory.copy()).run(inputs=[x+99,y-99], capture_output=True)
            if outputs[-1] == 1:
                box_fit = True
                print('(Part Two)')
                print(x * 10000 + y - 99)
            break
        x += 1
    if box_fit: break
    y += 1

print('~*~*~*~*~*~*~*~*~')
