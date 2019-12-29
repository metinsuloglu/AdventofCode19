#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 08:34:51 2019

@author: Metin Suloglu
"""

from collections import defaultdict

print('~*~*~ Day 24 ~*~*~')

def new_val(curr_val, num_adj):
    return (not curr_val and (num_adj == 1 or num_adj == 2)) or (curr_val and num_adj == 1)

def num_neighbours(loc, grid, recurse=False):
    if not grid: return 0
    assert not (recurse and loc[0] == 2 and loc[1] == 2)
    count = 0
    for direc in [(-1,0),(0,-1),(1,0),(0,1)]:
        new_loc = (loc[0] + direc[0], loc[1] + direc[1])
        if new_loc[0] >= 0 and new_loc[0] < 5 and new_loc[1] >= 0 and new_loc[1] < 5:
            if recurse and new_loc == (2, 2):
                if loc[0] == 2 and loc[1] == 1:
                    count += sum(grid[(x, 0, loc[2]+1)] for x in range(5))
                elif loc[0] == 2 and loc[1] == 3:
                    count += sum(grid[(x, 4, loc[2]+1)] for x in range(5))
                elif loc[1] == 2 and loc[0] == 1:
                    count += sum(grid[(0, y, loc[2]+1)] for y in range(5))
                elif loc[1] == 2 and loc[0] == 3:
                    count += sum(grid[(4, y, loc[2]+1)] for y in range(5))
            else: count += grid[(new_loc[0], new_loc[1], loc[2])]
        elif recurse:
            if new_loc[0] == -1:
                count += grid[(1, 2, loc[2]-1)]
            elif new_loc[0] == 5:
                count += grid[(3, 2, loc[2]-1)]
            if new_loc[1] == -1:
                count += grid[(2, 1, loc[2]-1)]
            elif new_loc[1] == 5:
                count += grid[(2, 3, loc[2]-1)]
    return count

def biodiversity_rating(grid, z):
    if not grid: return 0
    total = 0
    for y in range(5):
        for x in range(5):
            if grid[(x,y,z)]: total += 2**(5*y + x)
    return total

def count_bugs(grid):
    return sum(v for v in grid.values())


with open('day24.txt') as input_:
    eris = input_.read().splitlines()

orig_grid = defaultdict(int)
for line in range(len(eris)):
    for ch in range(len(eris[line])):
        orig_grid[(ch, line, 0)] = (eris[line][ch] == '#')
             
for p in range(1, 3):
    grid = orig_grid.copy()
    new_grid = orig_grid.copy()
    seen = set()
    n_mins = 0
    if p == 1: minZ, maxZ = 1, -1
    elif p == 2: minZ, maxZ = 0, 0
    while True:
        for z in range(minZ-1, maxZ+2):
            for y in range(5):
                for x in range(5):
                    if p == 2 and x == 2 and y == 2: continue
                    v = new_val(grid[(x, y, z)], num_neighbours((x, y, z), grid, recurse=(p==2)))
                    if p == 2 and v:
                        minZ = min(minZ, z)
                        maxZ = max(maxZ, z)
                    new_grid[(x, y, z)] = v
        grid = new_grid.copy()
        n_mins += 1
        
        state = frozenset([k for k, v in grid.items() if v])
        if p == 1:
            if state in seen:
                print('(Part One)')
                print(biodiversity_rating(grid, 0))
                break
            seen.add(state)
        if p == 2 and n_mins == 200:
            print('(Part Two)')
            print(count_bugs(grid))
            break
    
print('~*~*~*~*~*~*~*~*~')
