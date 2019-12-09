#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 06:47:47 2019

@author: Metin Suloglu
"""

from intcode import IntCode

print('~*~*~ Day 9 ~*~*~')

for p, i in zip(('One', 'Two'), (1, 2)):
    print('(Part ' + p + ')')
    IntCode('day9.csv').run(inputs=[i])
    
print('~*~*~*~*~*~*~*~*~')