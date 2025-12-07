import time
from functools import cache
import copy

solution_1 = 0
solution_2 = 0

st = time.time()

@cache
def particle_cached(manifold_map_tup, y, x):
    if y == len(manifold_map_tup):
        return 1
    
    timelines = 0
    
    if manifold_map_tup[y][x] == "^":        
        timelines += particle_cached(manifold_map_tup, y+1, x - 1) # Left path
        timelines += particle_cached(manifold_map_tup, y+1, x + 1) # Right path

    else:
        timelines += particle_cached(manifold_map_tup, y+1, x)

    return timelines

with open("7/input.txt", "r") as inpt:
    # manifold = np.array([[ch for ch in line if ch != "\n"] for line in inpt.readlines()])
    manifold = [[ch for ch in line if ch != "\n"] for line in inpt.readlines()]
    manifold_copy = copy.deepcopy(manifold)    
    

# Part 1
for y in range(1, len(manifold)):
    for beam in [i for i, el in enumerate(manifold[y-1]) if (el == "S" or el == "|")]:
        if manifold[y][beam] == "^":
            manifold[y][beam - 1] = "|"
            manifold[y][beam + 1] = "|"
            solution_1 += 1
        else:
            manifold[y][beam] = "|"
    # print(f"{y:3}", manifold[y])

# Part 2
solution_2 = particle_cached(tuple(map(tuple, manifold_copy)), 1, len(manifold_copy[0]) // 2)

t = time.time() - st
print("\n", "=" * 30, sep="")
print(f"Part 1: {solution_1} - {solution_1 == 21}")
print(f"Part 2: {solution_2} - {solution_2 == 40}")
print("=" * 30,  sep="")
print(f"t: {t:.4f} \n")

