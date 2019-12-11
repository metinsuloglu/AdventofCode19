#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 06:26:12 2019

@author: Metin Suloglu
"""

import numpy as np
from collections import defaultdict
from intcode import IntCode

print('~*~*~ Day 11 ~*~*~')

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for p in range(2):
    colour = defaultdict(int)
    curr_loc, curr_dir = (0, 0), 0
    if p == 1: colour[curr_loc] = 1

    brain = IntCode('day11.csv')
    painted = set()
    hc = 0
    minX, minY, maxX, maxY = [float('inf')] * 2 + [float('-inf')] * 2
    while hc != 99:
        _, outputs, hc = brain.run(inputs=[colour[curr_loc]], capture_output=True)
        colour[curr_loc] = outputs[0]
        painted.add(curr_loc)
        curr_dir = (curr_dir - 1) % 4 if outputs[1] == 0 else (curr_dir + 1) % 4
        curr_loc = (curr_loc[0] + dirs[curr_dir][0], curr_loc[1] + dirs[curr_dir][1])
        minX, minY = min(minX, curr_loc[0]), min(minY, curr_loc[1])
        maxX, maxY = max(maxX, curr_loc[0]), max(maxY, curr_loc[1])
        
    if p == 0:
        print('(Part One)')
        print(len(painted))
        continue
    
    print('(Part Two)')
    hull = np.zeros(((maxY - minY + 1), (maxX - minX + 1)))
    for coord in painted:
        hull[maxY - coord[1], coord[0] - minX] = colour[coord]
    for row in hull:
        print(''.join(['88' if c==1 else '  ' for c in row]))
    
print('~*~*~*~*~*~*~*~*~')
