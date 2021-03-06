#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Metin Suloglu
"""

import csv

class IntCode:
    
    def __init__(self, memory, i=0, mem_vals=None):
       self.opcode_params = {1:3, 2:3, 3:1, 4:1, 5:2, 6:2, 7:3, 8:3, 9:1, 99:0}
       if type(memory) is list: self.program = memory
       else: self.program = IntCode.read_memory(memory)
       self.program += [0] * 5 * len(self.program)
       self.i = i
       self.relative_base = 0
       if mem_vals is not None:
           for key, value in mem_vals.items():
               self.program[key] = value
    
    @staticmethod
    def read_memory(filename):
        with open(filename) as input_:
            memory = [int(n) for n in next(csv.reader(input_))]
        return memory
    
    def parse(self, val):
        modes = []
        rest = val//100
        opcode = val - rest*100
        for _ in range(self.opcode_params[opcode]):
            modes.append(rest % 10)
            rest //= 10
        return opcode, modes
    
    def getVal(self, i, mode):
        if mode == 0:
            return self.program[i]
        elif mode == 1:
            return i
        else:
            return self.program[i] + self.relative_base
    
    def run(self, inputs=None, capture_output=False):
        input_num = 0
        outputs = []
        while self.i < len(self.program):
            (opcode, modes) = self.parse(self.program[self.i])
            if opcode == 1:
                self.program[self.getVal(self.i+3, modes[2])] = self.program[self.getVal(self.i+1, modes[0])] + self.program[self.getVal(self.i+2, modes[1])]
            elif opcode == 2:
                self.program[self.getVal(self.i+3, modes[2])] = self.program[self.getVal(self.i+1, modes[0])] * self.program[self.getVal(self.i+2, modes[1])]
            elif opcode == 3:
                if inputs is None:
                    self.program[self.getVal(self.i+1, modes[0])] = int(input('Input: '))
                elif input_num >= len(inputs):
                    halt_code = 0
                    break
                else:
                    self.program[self.getVal(self.i+1, modes[0])] = int(inputs[input_num])
                    input_num += 1
            elif opcode == 4:
                if capture_output:
                    outputs.append(self.program[self.getVal(self.i+1, modes[0])])
                else:
                    print(self.program[self.getVal(self.i+1, modes[0])])
            elif opcode == 5:
                if self.program[self.getVal(self.i+1, modes[0])] != 0:
                    self.i = self.program[self.getVal(self.i+2, modes[1])] - self.opcode_params[opcode] - 1
            elif opcode == 6:
                if self.program[self.getVal(self.i+1, modes[0])] == 0:
                    self.i = self.program[self.getVal(self.i+2, modes[1])] - self.opcode_params[opcode] - 1
            elif opcode == 7:
                self.program[self.getVal(self.i+3, modes[2])] = int(self.program[self.getVal(self.i+1, modes[0])] < self.program[self.getVal(self.i+2, modes[1])])
            elif opcode == 8:
                self.program[self.getVal(self.i+3, modes[2])] = int(self.program[self.getVal(self.i+1, modes[0])] == self.program[self.getVal(self.i+2, modes[1])])
            elif opcode == 9:
                self.relative_base += self.program[self.getVal(self.i+1, modes[0])]
            elif opcode == 99:
                halt_code = 99
                break
            else:
                print('Unknown opcode.')
                halt_code = -1
                break
            self.i += self.opcode_params[opcode] + 1
        return self.program[0], outputs, halt_code