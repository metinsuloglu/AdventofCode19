#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 06:54:30 2019

@author: Metin Suloglu
"""

import math
import numpy as np
from collections import defaultdict

print('~*~*~ Day 10 ~*~*~')

asteroid_locs = set()
y = 0
with open('day10.txt') as input_:
    for line in input_.read().splitlines():
        asteroid_locs.update([(x, y) for x in np.argwhere(np.array(list(line))=='#')[:,0]])
        y += 1
        
best_detect, best_station, best_slopes = float('-inf'), None, defaultdict(list)
for station in asteroid_locs:
    asteroids = asteroid_locs - {station}
    slopes = defaultdict(list)
    for asteroid in asteroids:
        asteroid_trans = np.multiply(np.subtract(asteroid, station), (1, -1))
        slopes[math.atan2(asteroid_trans[1], asteroid_trans[0])].append(asteroid_trans)
    if len(slopes) > best_detect:
        best_detect = len(slopes)
        best_station = station
        best_slopes = slopes

print('(Part One)')
print(best_detect)

vaporised = 0
angles = list(best_slopes.keys())
angles.sort(reverse=True)
split_ind = next(i for i, a in enumerate(angles) if a <= math.pi/2) 
angles = angles[split_ind:] + angles[:split_ind]
while len(best_slopes) > 0:
    for a in angles:
        if len(best_slopes[a]) == 0:
            continue
        best_slopes[a].sort(key=lambda c: c[0]**2 + c[1]**2)
        vaporised_asteroid = best_slopes[a].pop(0)
        vaporised += 1
        if vaporised == 200:
            asteroid = (best_station[0] + vaporised_asteroid[0], best_station[1] - vaporised_asteroid[1])
            print('(Part Two)')
            print(asteroid[0] * 100 + asteroid[1])
            best_slopes.clear()
            break

print('~*~*~*~*~*~*~*~*~')
