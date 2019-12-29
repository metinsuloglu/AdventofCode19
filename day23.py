#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 07:47:05 2019

@author: Metin Suloglu
"""

from intcode import IntCode

print('~*~*~ Day 23 ~*~*~')

def send_packets(memory):
    computers = [IntCode(memory.copy()) for i in range(50)]
    qs = {c:[c] for c in range(len(computers))}
    found = False
    seen_y = set()
    while True:
        idle_count = 0
        for c in range(len(computers)):
            if not qs[c]: qs[c].append(-1)
            _, outputs, _ = computers[c].run(inputs=qs[c], capture_output=True)
            if qs[c] == [-1] and not outputs: idle_count += 1
            qs[c].clear()
            for j in range(0, len(outputs), 3):
                if outputs[j] == 255:
                    if not found:
                        print('(Part One)')
                        print(outputs[j + 2])
                        found = True
                    NAT = (outputs[j+1], outputs[j+2])
                else: qs[outputs[j]].extend([outputs[j+1], outputs[j+2]])
        if idle_count == len(computers):
            if NAT[1] in seen_y:
                print('(Part Two)')
                print(NAT[1])
                return
            qs[0].extend([NAT[0], NAT[1]])
            seen_y.add(NAT[1])


memory = IntCode.read_memory('day23.csv')
send_packets(memory)

print('~*~*~*~*~*~*~*~*~')
