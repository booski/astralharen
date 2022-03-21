#!/usr/bin/env python3

import random
import time

def print_state(holes, you, hare):
    symbols = {you:   '*',
               hare: '&'}
    if you == hare:
        symbols[you] = '!'
    print('[', end='')
    for hole in holes:
        print(symbols.get(hole, '.'), end='')
    print(']')

class Astralharen:
    def __init__(self, holes):
        self.holes = range(holes)
        self.mystep = 1
        self.turning = False
        self.steps = 0
    
    def jump(self, hare):
        if hare == self.holes[-1]:
            return hare - 1
        if hare == self.holes[0]:
            return hare + 1
        return random.choice([hare - 1,
                              hare + 1])

    def step(self, you):
        if self.turning:
            self.turning = False
            return you
        you += self.mystep
        if you >= self.holes[-1]:
            you = self.holes[-1]
            self.mystep = -self.mystep
            self.turning = True
        if you <= self.holes[0]:
            you = self.holes[0]
            self.mystep = -self.mystep
            self.turning = True
        return you
        
    def __call__(self):
        steps = 0
        you = 0
        hare = random.choice(self.holes)
        
        print('You: *    Hare: &'.center(len(self.holes)))
        print_state(self.holes, you, hare)
        input('Press enter to start searching')
        while you != hare:
            steps += 1
            print_state(self.holes, you, hare)

            hare = self.jump(hare)
            you = self.step(you)
            time.sleep(0.2)
            
        print_state(self.holes, you, hare)
        print(f'Found in {steps} steps.')

Astralharen(50)()
