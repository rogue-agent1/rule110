#!/usr/bin/env python3
"""Rule 110 — Turing-complete elementary cellular automaton."""
import sys

def rule_table(rule_num):
    return {tuple(int(b) for b in f"{i:03b}"): (rule_num >> i) & 1 for i in range(8)}

def simulate(width=80, steps=40, rule_num=110, init=None):
    table = rule_table(rule_num)
    if init is None:
        state = [0]*width; state[-1] = 1
    else: state = init
    rows = [state[:]]
    for _ in range(steps-1):
        new = [0]*width
        for i in range(width):
            l = state[(i-1)%width]; c = state[i]; r = state[(i+1)%width]
            new[i] = table[(l,c,r)]
        state = new; rows.append(state[:])
    return rows

def display(rows):
    for row in rows: print("".join("█" if c else " " for c in row))

def cli():
    rule = int(sys.argv[1]) if len(sys.argv)>1 else 110
    w = int(sys.argv[2]) if len(sys.argv)>2 else 80
    steps = int(sys.argv[3]) if len(sys.argv)>3 else 40
    print(f"Rule {rule} ({w}x{steps}):")
    display(simulate(w, steps, rule))

if __name__ == "__main__": cli()
