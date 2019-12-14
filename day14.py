#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 08:40:09 2019

@author: Metin Suloglu
"""

import math
from collections import defaultdict

print('~*~*~ Day 14 ~*~*~')

def num_ores(item, amount, curr, chemicals):
    if item == 'ORE': return amount
    usable = min(curr[item], amount)
    amount -= usable
    curr[item] -= usable
    min_val, min_num = [float('inf')] * 2
    for num in chemicals[item]:
        mult = math.ceil(amount / num)
        min_option = float('inf')
        for option in chemicals[item][num]:
            option_ores = 0
            for chem in option:
                option_ores += num_ores(chem[1], chem[0] * mult, curr, chemicals)
            min_option = min(min_option, option_ores)
        if min_option < min_val:
            min_val = min_option
            min_num = num
    curr[item] += math.ceil(amount / min_num) * min_num - amount
    return min_val

chemicals = defaultdict(lambda: defaultdict(list))
with open('day14.txt') as input_:
    lines = input_.read().splitlines()
    for line in lines:
        inp, out = [chem.split(', ') for chem in line.split(' => ')]
        inp = [(int(c[0]), c[1]) for c in [chem.split(' ') for chem in inp]]
        out = out[0].split(' ')
        chemicals[out[1]][int(out[0])].append(inp)

print('(Part One)')
print(num_ores('FUEL', 1, defaultdict(int), chemicals))

max_ore = int(1e12)
lower = 0
upper = 1000
while num_ores('FUEL', upper, defaultdict(int), chemicals) < max_ore:
    upper *= 10
while True:
    mid = (lower + upper) // 2
    if mid == lower: break
    if num_ores('FUEL', mid, defaultdict(int), chemicals) > max_ore: upper = mid
    else: lower = mid
    
print('(Part Two)')
print(lower)

print('~*~*~*~*~*~*~*~*~')
