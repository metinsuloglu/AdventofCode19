#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 09:21:53 2019

@author: Metin Suloglu
"""

from heapq import heappop, heappush

print('~*~*~ Day 18 ~*~*~')

def iskey(c):
    return 96 < ord(c) < 123

def isdoor(c):
    return 64 < ord(c) < 91

def isentrance(c):
    return c in {'@','0','1','2','3'}

def search_from(coord, tunnels, keys=None):
    path_info = {}
    found_keys = set()
    if not isentrance(tunnels[coord[1]][coord[0]]):
        found_keys.add(tunnels[coord[1]][coord[0]])
    s = [(coord, 0, set(), set())]
    seen = set()
    while s:
        curr = s.pop(0)
        if curr[0] not in seen:
            seen.add(curr[0])
            for direc in [(1,0),(0,1),(-1,0),(0,-1)]:
                neighbour = (curr[0][0] + direc[0], curr[0][1] + direc[1])
                c = tunnels[neighbour[1]][neighbour[0]]
                if c == '#': continue
                elif isdoor(c): 
                    s.append((neighbour, curr[1]+1, curr[2] | set(c), curr[3]))
                else:
                    if iskey(c):
                        if c not in found_keys:
                            path_info[c] = (curr[1] + 1, curr[2], curr[3])
                            found_keys.add(c)
                        s.append((neighbour, curr[1] + 1, curr[2], curr[3] | set(c)))
                    else:
                        s.append((neighbour, curr[1] + 1, curr[2], curr[3]))
        if keys is not None and found_keys == keys: break
    return path_info, found_keys

def get_path_info(tunnels):
    path_info = {}
    keys, entry_locs = None, []
    for y in range(len(tunnels)):
        for x in range(len(tunnels[y])):
            entrance = isentrance(tunnels[y][x])
            if entrance or iskey(tunnels[y][x]):
                path_info[tunnels[y][x]], keys = search_from((x, y), tunnels, keys=keys)
                if entrance: entry_locs.append((x, y))
    return path_info, keys, entry_locs

def search(entrances, path_info, keys):
    s = [(0, entrances, frozenset())]
    seen = set()
    while s:
        curr = heappop(s)
        state = (curr[1], curr[2])
        if state not in seen:
            seen.add(state)
            if curr[2] == keys:
                print('(Part One)' if len(entrances) == 1 else '(Part Two)')
                print(curr[0])
                break
            for r in range(len(curr[1])):
                for k, v in path_info[curr[1][r]].items():
                    if k not in curr[2] and set(d.lower() for d in v[1]) <= curr[2] and not (v[2] - curr[2]):
                        heappush(s, (curr[0] + v[0], curr[1][:r] + (k,) + curr[1][r+1:], curr[2] | set(k)))

with open('day18.txt') as input_:
    tunnels = input_.read().splitlines()

path_info, keys, entry_locs = get_path_info(tunnels)
search(('@',), path_info, keys)

entry_loc = entry_locs[0]
tunnels[entry_loc[1]-1] = tunnels[entry_loc[1]-1][:entry_loc[0]-1] + '0#1' + tunnels[entry_loc[1]-1][entry_loc[0]+2:]
tunnels[entry_loc[1]] = tunnels[entry_loc[1]][:entry_loc[0]-1] + '###' + tunnels[entry_loc[1]][entry_loc[0]+2:]
tunnels[entry_loc[1]+1] = tunnels[entry_loc[1]+1][:entry_loc[0]-1] + '2#3' + tunnels[entry_loc[1]+1][entry_loc[0]+2:]

path_info, _, _ = get_path_info(tunnels)
search(('0','1','2','3'), path_info, keys)

print('~*~*~*~*~*~*~*~*~')