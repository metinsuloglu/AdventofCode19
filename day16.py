#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 07:35:23 2019

@author: Metin Suloglu
"""

import numpy as np

print('~*~*~ Day 16 ~*~*~')

def FFT(signal, base_pattern, iters):
    length = len(signal)
    pattern = np.zeros((length, length), dtype='int')
    for col in range(length):
        pattern[:, col] = np.resize(np.repeat(base_pattern, col+1), length+1)[1:]
    for _ in range(iters):
        signal = abs(signal @ pattern) % 10
    return signal[:8]

def FFT_opt(signal, base_pattern, offset, iters):
    assert offset >= len(signal) / 2
    signal = signal[:offset-1:-1]
    for i in range(iters):
        signal = np.cumsum(signal) % 10
    return signal[:len(signal)-9:-1]


signal = np.genfromtxt('day16.txt', delimiter=1, dtype='int')
base_pattern = [0, 1, 0, -1]

new_list = FFT(signal, base_pattern, 100)
print('(Part One)')
print(np.array2string(new_list, separator='')[1:-1])

signal = np.tile(signal, 10000)
offset = int(np.array2string(signal[:7], separator='')[1:-1])

new_list = FFT_opt(signal, base_pattern, offset, 100)
print('(Part Two)')
print(np.array2string(new_list, separator='')[1:-1])

print('~*~*~*~*~*~*~*~*~')
