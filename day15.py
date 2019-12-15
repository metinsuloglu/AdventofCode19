#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 08:59:14 2019

@author: Metin Suloglu
"""

import numpy as np
from collections import defaultdict
from intcode import IntCode

print('~*~*~ Day 15 ~*~*~')

def make_map(droid):
    dirs = {1:(0,-1), 2:(0,1), 3:(-1,0), 4:(1,0)}
    reverse = {1:2, 2:1, 3:4, 4:3}
    
    s = []
    curr_loc = (0,0)
    remaining = defaultdict(lambda: set({1,2,3,4}))
    locs = defaultdict(lambda: 1)
    while True:
        if len(s):
            prev_move = s.pop()
            curr_loc = tuple(np.add(curr_loc, dirs[prev_move]))
            remaining[curr_loc].discard(reverse[prev_move])
        moved = False
        for i in set(remaining[curr_loc]):
            _, outputs, _ = droid.run(inputs=[i], capture_output=True)
            if outputs[0] == 0:
                locs[tuple(np.add(curr_loc, dirs[i]))] = 0
            else:
                s.extend([reverse[i], i])
                locs[tuple(np.add(curr_loc, dirs[i]))] = outputs[0]
                moved = True
            remaining[curr_loc].discard(i)
            if moved: break
        
        if not len(s): break
        if not moved:
            _, _, _ = droid.run(inputs=[s[-1]], capture_output=True)
            
    return locs

def bfs(area, initial_loc, target):
    s = [initial_loc]
    checked = set()
    time = 0
    while len(s):
        for _ in range(len(s)):
            curr = s.pop(0)
            checked.add(curr)
            for d in [(0,-1),(0,1),(-1,0),(1,0)]:
                neighbour = tuple(np.add(curr, d))
                if area[neighbour] != 0 and neighbour not in checked:
                    if area[neighbour] == target:
                        return neighbour, time + 1
                    s.append(neighbour)
        time += 1
    return time - 1


droid = IntCode('day15.csv')
area = make_map(droid)

print('(Part One)')
oxygen_loc, dist = bfs(area, (0,0), 2)
print(dist)

print('(Part Two)')
mins = bfs(area, oxygen_loc, None)
print(mins)

print('~*~*~*~*~*~*~*~*~')
