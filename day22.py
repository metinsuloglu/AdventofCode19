#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 08:06:33 2019

@author: Metin Suloglu
"""

print('~*~*~ Day 22 ~*~*~')

def deal(cards):
    cards.reverse()

def cut(cards, N):
    cards[:] = cards[N:]+cards[:N]

def deal_increment(cards, N):
    order = cards.copy()
    num_cards = len(cards)
    i = 0
    for j in range(num_cards):
        cards[i] = order[j]
        i = (i + N) % num_cards

with open('day22.txt') as input_:
    shuffle = input_.read().splitlines()

cards = list(range(10007))
for func in shuffle:
    if func.startswith('cut'):
        cut(cards, int(func[4:]))
    elif func.startswith('deal with increment'):
        deal_increment(cards, int(func[20:]))
    elif func == 'deal into new stack':
        deal(cards)

print('(Part One)')
print(cards.index(2019))

print('~*~*~*~*~*~*~*~*~')
