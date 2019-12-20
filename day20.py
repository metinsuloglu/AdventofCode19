#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 07:53:06 2019

@author: Metin Suloglu
"""

from collections import defaultdict

print('~*~*~ Day 20 ~*~*~')

with open('day20.txt') as input_:
    maze = input_.read().splitlines()

s = []
portal_coords, coord_portals = defaultdict(list), defaultdict(list)
outer = set()
for y in range(len(maze)):
    for x in range(len(maze[y])):
        if 64 < ord(maze[y][x]) < 91:
            for direc in [(0,1),(-1,0),(0,-1),(1,0)]:
                n_x, n_y = x + direc[0], y+direc[1]
                nn_x, nn_y = n_x + direc[0], n_y + direc[1]
                if nn_x < 0 or nn_y < 0 or nn_x >= len(maze[y]) or nn_y >= len(maze): continue
                if 64 < ord(maze[n_y][n_x]) < 91 and maze[nn_y][nn_x] == '.':
                    if direc[0] == -1 or direc[1] == -1: name = maze[n_y][n_x] + maze[y][x]
                    else: name = maze[y][x] + maze[n_y][n_x]
                    portal_coords[name].append((nn_x, nn_y))
                    coord_portals[(nn_x, nn_y)].append(name)
                    if name == 'AA': s.append(((nn_x, nn_y), 0, 0))
                    elif name == 'ZZ': continue
                    elif (nn_y == 2 or nn_y == len(maze)-3 or nn_x == 2 or nn_x == len(maze[y])-3):
                        outer.add((nn_x, nn_y))

seen = set()
found = [False, False]
while len(s):
    curr = s.pop(0)
    if (curr[0], curr[2]) not in seen:
        seen.add((curr[0], curr[2]))
        for direc in [(0,1),(-1,0),(0,-1),(1,0)]:
            n_coord = (curr[0][0] + direc[0], curr[0][1] + direc[1])
            if maze[n_coord[1]][n_coord[0]] == '.': s.append(((n_coord), curr[1] + 1, curr[2]))
        if curr[0] in coord_portals:
            for n in coord_portals[curr[0]]:
                if n == 'ZZ':
                    if curr[2] == 0 and not found[1]:
                        print('(Part Two)')
                        print(curr[1])
                        found[1] = True
                    if not found[0]:
                        print('(Part One)')
                        print(curr[1])
                        found[0] = True
                elif n == 'AA': continue
                elif curr[0] in outer and curr[2] > 0:
                    s.append(((list(set(portal_coords[n]) - {curr[0]})[-1]), curr[1] + 1, curr[2] - 1))
                elif curr[0] not in outer:
                    s.append(((list(set(portal_coords[n]) - {curr[0]})[-1]), curr[1] + 1, curr[2] + 1))
    if all(found): break

print('~*~*~*~*~*~*~*~*~')
