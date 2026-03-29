#!/usr/bin/env python3
"""rule110 - Elementary cellular automaton (Rule 110 etc)."""
import sys, argparse, json

def step(cells, rule):
    n = len(cells)
    new = [0] * n
    for i in range(n):
        left = cells[(i-1) % n]
        center = cells[i]
        right = cells[(i+1) % n]
        pattern = (left << 2) | (center << 1) | right
        new[i] = (rule >> pattern) & 1
    return new

def simulate(width, generations, rule=110, init="center"):
    cells = [0] * width
    if init == "center": cells[width//2] = 1
    elif init == "random":
        import random; cells = [random.randint(0,1) for _ in range(width)]
    history = [cells[:]]
    for _ in range(generations - 1):
        cells = step(cells, rule)
        history.append(cells[:])
    return history

def render(history):
    return "
".join("".join("█" if c else " " for c in row) for row in history)

def main():
    p = argparse.ArgumentParser(description="Cellular automaton")
    p.add_argument("--rule", type=int, default=110)
    p.add_argument("--width", type=int, default=80)
    p.add_argument("--generations", type=int, default=40)
    p.add_argument("--init", choices=["center","random"], default="center")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    history = simulate(args.width, args.generations, args.rule, args.init)
    if args.json:
        alive = sum(sum(row) for row in history)
        print(json.dumps({"rule": args.rule, "width": args.width, "generations": args.generations, "alive_cells": alive}))
    else:
        print(f"Rule {args.rule}:")
        print(render(history))

if __name__ == "__main__": main()
