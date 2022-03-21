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
    def __init__(self, holes, step):
        self.holes = range(holes)
        self.stepsize = step
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
        you += self.stepsize
        if you >= self.holes[-1]:
            you = self.holes[-1]
            self.stepsize = -self.stepsize
            self.turning = True
        if you <= self.holes[0]:
            you = self.holes[0]
            self.stepsize = -self.stepsize
            self.turning = True
        return you
        
    def __call__(self):
        steps = 0
        you = 0
        hare = random.choice(self.holes)
        
        while you != hare:
            steps += 1
            print_state(self.holes, you, hare)

            hare = self.jump(hare)
            you = self.step(you)
            time.sleep(0.1)
            
        print_state(self.holes, you, hare)
        print('You: *, Hare: &, Found: !'.center(len(self.holes)))
        print(f'Found in {steps} steps.')

if __name__ == '__main__':
    Astralharen(50, 1)()
