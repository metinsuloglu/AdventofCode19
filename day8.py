#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 08:46:36 2019

@author: Metin Suloglu
"""

import numpy as np

print('~*~*~ Day 8 ~*~*~')

def view_message(image):
    layers = np.dsplit(image, image.shape[2])
    return np.select([layer < 2 for layer in layers], layers).squeeze()

image = np.genfromtxt('day8.txt', delimiter=1, dtype='int').reshape(25,6,-1, order='F').transpose(1,0,2)
min_layer = np.argmin(np.count_nonzero(image==0, axis=(0,1)))

print('(Part One)')
print(np.count_nonzero(image[:,:,min_layer]==1) * np.count_nonzero(image[:,:,min_layer]==2))

print('(Part Two)')
for row in view_message(image):
    print(''.join(['88' if c==1 else '  ' for c in row]))
    
print('~*~*~*~*~*~*~*~*~')