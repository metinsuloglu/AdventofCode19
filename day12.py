#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 07:38:38 2019

@author: Metin Suloglu
"""

import numpy as np
from itertools import combinations

print('~*~*~ Day 12 ~*~*~')

positions = np.array([[3,3,0],[4,-16,2],[-10,-6,5],[-3,0,-13]], dtype='int')
velocities = np.zeros((4, 3), dtype='int')

step = 0
seen, periods, axes = [set(), set(), set()], [-1] * 3, list(range(3))
states = np.concatenate((positions, velocities))
for ax in axes:
    seen[ax].add(tuple(states[:,ax]))
while len(axes) > 0:
    step += 1
    for m1, m2 in combinations(range(len(positions)), 2):
        change = np.sign(positions[m1] - positions[m2])
        velocities[m1] = np.add(velocities[m1], -change)
        velocities[m2] = np.add(velocities[m2], change)
    positions = np.add(positions, velocities)
    if step == 1000:
        print('(Part One)')
        print(sum(np.multiply(np.sum(abs(positions), axis=1), np.sum(abs(velocities), axis=1))))
    states = np.concatenate((positions, velocities))
    for ax in axes:
        state = tuple(states[:,ax])
        if state in seen[ax]:
            periods[ax] = step
            axes.remove(ax)
            continue
        seen[ax].add(state)

print('(Part Two)')
print(np.lcm.reduce(periods))

print('~*~*~*~*~*~*~*~*~')
