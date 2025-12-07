import time
import re
from functools import reduce
import numpy as np

solution_1 = 0
solution_2 = 0

st = time.time()

with open("7/input.txt", "r") as inpt:
    manifold = np.array([[ch for ch in line if ch != "\n"] for line in inpt.readlines()])
    # manifold = [line.replace("\n", "") for line in inpt.readlines()]

print(manifold)

#          [x, y - 1]
# [x - 1, y] [x, y] [x + 1, y]
#          [x, y + 1]
 
for y in range(1, len(manifold)):
    for beam in [i for i, el in enumerate(manifold[y-1]) if (el == "S" or el == "|")]:
        if manifold[y][beam] == "^":
            manifold[y][beam - 1] = "|"
            manifold[y][beam + 1] = "|"
            solution_1 += 1
        else:
            manifold[y][beam] = "|"
    # print(f"{y:3}", manifold[y])
    
print(manifold)   
    
t = time.time() - st
print("\n", "=" * 30, sep="")
print(f"Part 1: {solution_1} - {solution_1 == 6171290547579}")
print(f"Part 2: {solution_2} - {solution_2 == 8811937976367}")
# print(solution)
print("=" * 30,  sep="")
print(f"t: {t:.4f} \n")

