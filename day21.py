#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 09:48:34 2019

@author: Metin Suloglu
"""

from intcode import IntCode

print('~*~*~ Day 21 ~*~*~')

memory = IntCode.read_memory('day21.csv')
springdroid = IntCode(memory.copy())
inst = ['NOT C J','NOT B T','OR T J',
        'NOT A T','OR T J','AND D J',
        'WALK\n']
_, outputs, _ = springdroid.run(inputs=[ord(c) for c in '\n'.join(inst)], capture_output=True)
print('(Part One)')
print(outputs[-1])

springdroid = IntCode(memory.copy())
inst[6:7] = ['NOT E T','NOT T T','OR H T','AND T J','RUN\n']
_, outputs, _ = springdroid.run(inputs=[ord(c) for c in '\n'.join(inst)], capture_output=True)
print('(Part Two)')
print(outputs[-1])

print('~*~*~*~*~*~*~*~*~')
