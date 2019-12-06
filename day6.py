#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 08:11:22 2019

@author: Metin Suloglu
"""

from collections import defaultdict

print('~*~*~ Day 6 ~*~*~')

with open('day6.txt','r') as input_:
    orbits = defaultdict(list)
    for o in [orbit.split(')') for orbit in input_.read().splitlines()]:
        orbits[o[0]].append(o[1])
        orbits[o[1]].append(o[0])
    
def dfs(orbits):
    checked = set()
    count = 0
    s = []
    s.append(('COM',0))
    while len(s) != 0:
        curr = s.pop()
        checked.add(curr[0])
        count += curr[1]
        s.extend([(orbit, curr[1]+1) for orbit in orbits[curr[0]] if orbit not in checked])
    
    return count

def find_santa(orbits):
    checked = set()
    count = 0
    s = []
    s.append(('YOU',0))
    while len(s) != 0:
        curr = s.pop(0)
        checked.add(curr[0])
        count += 1
        for orbit in orbits[curr[0]]:
            if orbit not in checked:
                s.append((orbit, curr[1]+1))
                if orbit == 'SAN':
                    return curr[1] - 1
    return -1

print('(Part One)')
print(dfs(orbits))

print('(Part Two)')
print(find_santa(orbits))
       
        