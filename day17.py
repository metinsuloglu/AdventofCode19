#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:48:52 2019

@author: Metin Suloglu
"""

import numpy as np
from collections import defaultdict
from intcode import IntCode

print('~*~*~ Day 17 ~*~*~')

def neighbours(coord, scaffolds):
    for d in [(0,-1),(0,1),(1,0),(-1,0)]:
        neighbour = tuple(np.add(coord, d))
        if neighbour in scaffolds:
            yield scaffolds[neighbour]

def compress(path, assigned={}, c_remain=['A','B','C']):
    if not len(path): return path, assigned
    seq, best_assigned = None, {}
    for i in range(1, min(len(path) + 1, 10)):
        test_string = ','.join([str(c) for c in path[:i]])
        if len(test_string) >= 20: break
        assigned_iter = assigned.copy()
        if test_string not in assigned:
            if not len(c_remain): continue
            assigned_iter[test_string] = c_remain[0]
            rest = compress(path[i:], assigned_iter, c_remain[1:])
        else:
            rest = compress(path[i:], assigned, c_remain)
        if rest[0] is not None:
            if seq is None or len(rest[0]) < len(seq) - 1:
                seq = [assigned_iter[test_string]] + rest[0]
                best_assigned = assigned_iter.copy()
                best_assigned.update(rest[1])
    return seq, best_assigned

memory = IntCode.read_memory('day17.csv')
camera = IntCode(memory.copy())
scaffolds = defaultdict(lambda: '.')
_, outputs, _ = camera.run(capture_output=True)

dir_map = {'^':0, '>':1, 'v':2, '<':3}
dir_coord = {0:(0,-1), 1:(1,0), 2:(0,1), 3:(-1,0)}
x, y = 0, 0
for o in outputs:
    if o == 10:
        x = 0
        y += 1
    else:
        ch = chr(o)
        if ch in dir_map:
            curr_dir = dir_map[ch]
            curr_coord = (x, y)
        scaffolds[(x, y)] = ch
        x += 1

align_param = 0
for coord, i in scaffolds.items():
    if i == '#' and all(n == '#' for n in neighbours(coord, scaffolds)):
        align_param += coord[0] * coord[1]
        
print('(Part One)')
print(align_param)

robot = IntCode(memory, mem_vals={0:2})
seq = []
forw_count = 0
while True:
    forw_coord = tuple(np.add(curr_coord, dir_coord[curr_dir]))
    if scaffolds[forw_coord] == '.':
        if forw_count > 0: 
            seq.append(forw_count)
            forw_count = 0
        left_dir, right_dir = (curr_dir - 1) % 4, (curr_dir + 1) % 4
        left = tuple(np.add(curr_coord, dir_coord[left_dir]))
        right = tuple(np.add(curr_coord, dir_coord[right_dir]))
        if scaffolds[left] == '#':
            seq.extend(['L'])
            curr_dir = left_dir
        elif scaffolds[right] == '#':
            seq.extend(['R'])
            curr_dir = right_dir
        else: break
    else:
        forw_count += 1
        curr_coord = forw_coord

seq, assigned = compress(seq)
seq = ','.join(seq) + '\n'
assigned = {v:k for k, v in assigned.items()}
_, outputs, _ = robot.run(inputs=list(map(ord, seq)), capture_output=True)
for func in ['A','B','C']:
    _, outputs, _ = robot.run(inputs=list(map(ord, assigned[func] + '\n')), capture_output=True)
_, outputs, _ = robot.run(inputs=list(map(ord, 'n\n')), capture_output=True)

print('(Part Two)')
print(outputs[-1])

print('~*~*~*~*~*~*~*~*~')
