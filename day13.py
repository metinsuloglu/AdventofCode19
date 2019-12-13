#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 07:35:29 2019

@author: Metin Suloglu
"""

import numpy as np
from intcode import IntCode

def play(arcade):
    _, outputs, _ = arcade.run(inputs=[], capture_output=True)
    score = 0
    while len(outputs):
        for o in [outputs[i:i+3] for i in range(0, len(outputs), 3)]:
            if o[0] == -1 and o[1] == 0: score = o[2]
            elif o[2] == 3: paddle_loc = o[0]
            elif o[2] == 4: ball_loc = o[0]
        _, outputs, _ = arcade.run(inputs=[np.sign(ball_loc - paddle_loc)], capture_output=True)
    return score

memory = IntCode.read_memory('day13.csv')

arcade = IntCode(memory.copy())
_, outputs, _ = arcade.run(inputs=[], capture_output=True)
count = 0
for o in [outputs[i:i+3] for i in range(0, len(outputs), 3)]:
    count += (o[2] == 2)
print(count)

arcade = IntCode(memory.copy(), mem_vals={0:2})
score = play(arcade)
print(score)