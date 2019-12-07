#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 09:52:50 2019

@author: Metin Suloglu
"""

from intcode import IntCode

print('~*~*~ Day 5 ~*~*~')

memory = IntCode.read_memory('day5.csv')

print('(Part One)')
_, _, _ = IntCode(memory.copy()).run(inputs=[1])

print('(Part Two)')
_, _, _ = IntCode(memory.copy()).run(inputs=[5])

print('~*~*~*~*~*~*~*~*~')