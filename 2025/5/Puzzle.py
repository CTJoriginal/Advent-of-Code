import time
import re
import numpy as np

solution_1 = 0
solution_2 = 0

st = time.time()

with open("5/input.txt", "r") as inpt:
    inpt = inpt.read()
    ranges = [(int(d1), int(d2)) for d1, d2 in re.findall(r"^(\d+)-(\d+)$", inpt, re.MULTILINE)]
    ranges = sorted(ranges)
    items = [int(d) for d in re.findall(r"^\d+$", inpt, re.MULTILINE)]

# Part 1
for item in items:
    for low, high in ranges:
        if item >= low and item <= high:
            solution_1 += 1
            break

# Part 2
solution = []

for start, stop in ranges:
    # Check each solution range
    for i, rng in enumerate(solution):
        if start in rng or start == rng.stop: # If range start overlaps (this also captures all fully contained ranges)
            if stop - 1 not in rng: 
                solution[i] = range(rng.start, stop)
            break    
    else: # for...else *loop* - else statement is triggered if loop is not broken
        solution.append(range(start, stop))

t = time.time() - st

print("\n", "=" * 30, sep="")
print(f"Part 1: {solution_1}")
print(f"Part 2: {sum([len(r) + 1 for r in solution])}")
# print(solution)
print("=" * 30,  sep="")
print(f"t: {t:.4f} \n")

