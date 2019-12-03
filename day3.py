#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 07:06:53 2019

@author: Metin Suloglu
"""

import csv
from collections import defaultdict

print('~*~*~ Day 3 ~*~*~')

with open('day3.csv') as input_:
    wires = list(csv.reader(input_))
    
directions = {'R':(1,0),'L':(-1,0),'U':(0,1),'D':(0,-1)}
steps = [defaultdict(lambda: float('inf')), defaultdict(lambda: float('inf'))]
for i, paths in enumerate(wires):
    curr_coord = (0, 0)
    time = 0
    for path in paths:
        direc, dist = path[:1], int(path[1:])
        for _ in range(1, dist+1):
            time += 1
            curr_coord = tuple(sum(c) for c in zip(curr_coord, directions[direc]))
            steps[i][curr_coord] = min(steps[i][curr_coord], time)
        
crossings = set(steps[0]).intersection(set(steps[1]))

print('(Part One)')
print(min([abs(x) + abs(y) for x, y in crossings]))

print('(Part Two)')
print(min([steps[0][coord] + steps[1][coord] for coord in crossings]))