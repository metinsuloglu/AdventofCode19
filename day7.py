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
for (A,B,C,D,E) in permutations(range(0, 5)):
    _, outputs, _ = IntCode(memory.copy()).run(inputs=[A, 0], capture_output=True)
    _, outputs, _ = IntCode(memory.copy()).run(inputs=[B] + outputs, capture_output=True)
    _, outputs, _ = IntCode(memory.copy()).run(inputs=[C] + outputs, capture_output=True)
    _, outputs, _ = IntCode(memory.copy()).run(inputs=[D] + outputs, capture_output=True)
    _, outputs, _ = IntCode(memory.copy()).run(inputs=[E] + outputs, capture_output=True)
    
    max_signal = max(outputs[0], max_signal)

print('(Part One)')
print(max_signal)

max_signal = -float('inf')
for (A,B,C,D,E) in permutations(range(5, 10)):
    amps = [IntCode(memory.copy()) for _ in range(5)]
    _, outputs, hc = amps[0].run(inputs=[A, 0], capture_output=True)
    _, outputs, hc = amps[1].run(inputs=[B] + outputs, capture_output=True)
    _, outputs, hc = amps[2].run(inputs=[C] + outputs, capture_output=True)
    _, outputs, hc = amps[3].run(inputs=[D] + outputs, capture_output=True)
    _, outputs, hc = amps[4].run(inputs=[E] + outputs, capture_output=True)
    while hc != 99:
        _, outputs, hc = amps[0].run(inputs=outputs, capture_output=True)
        _, outputs, hc = amps[1].run(inputs=outputs, capture_output=True)
        _, outputs, hc = amps[2].run(inputs=outputs, capture_output=True)
        _, outputs, hc = amps[3].run(inputs=outputs, capture_output=True)
        _, outputs, hc = amps[4].run(inputs=outputs, capture_output=True)
    
    max_signal = max(outputs[0], max_signal)

print('(Part Two)')
print(max_signal)

print('~*~*~*~*~*~*~*~*~')