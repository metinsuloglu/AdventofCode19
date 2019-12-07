#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 08:29:27 2019

@author: Metin Suloglu
"""

from itertools import permutations 
from intcode import IntCode

print('~*~*~ Day 7 ~*~*~')

memory = IntCode.read_memory('day7.csv')
    
max_signal = -float('inf')
for p in permutations(range(0, 5)):
    outputs = [0]
    for amp in range(5):
        _, outputs, _ = IntCode(memory.copy()).run(inputs=[p[amp]] + outputs, capture_output=True)
    
    max_signal = max(outputs[0], max_signal)

print('(Part One)')
print(max_signal)

max_signal = -float('inf')
for p in permutations(range(5, 10)):
    amps = [IntCode(memory.copy()) for _ in range(5)]
    outputs = [0]
    for amp in range(5):
        _, outputs, hc = amps[amp].run(inputs=[p[amp]] + outputs, capture_output=True)
    while hc != 99:
        for amp in range(5):
            _, outputs, hc = amps[amp].run(inputs=outputs, capture_output=True)
    
    max_signal = max(outputs[0], max_signal)

print('(Part Two)')
print(max_signal)

print('~*~*~*~*~*~*~*~*~')