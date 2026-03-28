#!/usr/bin/env python3
"""rule110 - Rule 110 elementary cellular automaton (Turing complete)."""
import sys
def evolve(rule_num, width, generations):
    rule = {tuple(int(b) for b in format(i, '03b')): (rule_num >> i) & 1 for i in range(8)}
    state = [0] * width; state[width//2] = 1
    for _ in range(generations):
        print("".join("█" if c else " " for c in state))
        new = [0] * width
        for i in range(width):
            left = state[(i-1) % width]; center = state[i]; right = state[(i+1) % width]
            new[i] = rule[(left, center, right)]
        state = new
if __name__ == "__main__":
    rule = int(sys.argv[1]) if len(sys.argv) > 1 else 110
    width = int(sys.argv[2]) if len(sys.argv) > 2 else 80
    gens = int(sys.argv[3]) if len(sys.argv) > 3 else 40
    evolve(rule, width, gens)
