#!/usr/bin/env python3
"""Elementary cellular automaton (Rule 110 and others)."""
import sys

def step(cells, rule=110):
    n = len(cells); new = [0]*n
    for i in range(n):
        pattern = (cells[(i-1)%n] << 2) | (cells[i] << 1) | cells[(i+1)%n]
        new[i] = (rule >> pattern) & 1
    return new

def run(width=80, generations=40, rule=110, seed=None):
    cells = [0]*width
    if seed: 
        for i in seed: cells[i % width] = 1
    else:
        cells[width-1] = 1
    for g in range(generations):
        print(''.join('█' if c else ' ' for c in cells))
        cells = step(cells, rule)

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('-r', '--rule', type=int, default=110)
    p.add_argument('-w', '--width', type=int, default=80)
    p.add_argument('-g', '--generations', type=int, default=40)
    args = p.parse_args()
    run(args.width, args.generations, args.rule)
