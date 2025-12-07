import time
import re
from functools import reduce
# import numpy as np
from functools import cache
import copy

solution_1 = 0
solution_2 = 0

st = time.time()

def to_tuple(arr):
    return tuple(map(tuple, arr))

def particle(manifold_map, y):
    if y == len(manifold_map):
        # print(manifold_map, "\n")
        return 1
    
    timelines = 0
    for beam, el in enumerate(manifold_map[y-1]):
        if el not in ("S", "|"):
            continue
        
        if manifold_map[y][beam] == "^":
            left_path = copy.deepcopy(manifold_map)
            right_path = copy.deepcopy(manifold_map)
            
            left_path[y][beam - 1] = "|"
            right_path[y][beam + 1] = "|"
            
            # timelines += 1 # This timeline split
            timelines += particle(left_path, y+1) # Get number of splits on Left path
            timelines += particle(right_path, y+1) # Left path

        else:
            path = copy.deepcopy(manifold_map)
            path[y][beam] = "|"
            timelines += particle(path, y+1)

    return timelines

@cache
def particle_cached(manifold_map_tup, y):
    if y == len(manifold_map_tup):
        # print(manifold_map, "\n")
        return 1
    
    manifold_map = [list(row) for row in manifold_map_tup]
    
    timelines = 0
    for beam, el in enumerate(manifold_map[y-1]):
        if el not in ("S", "|"):
            continue
        
        if manifold_map[y][beam] == "^":
            left_path = copy.deepcopy(manifold_map)
            right_path = copy.deepcopy(manifold_map)
            
            left_path[y][beam - 1] = "|"
            right_path[y][beam + 1] = "|"
            
            timelines += particle_cached(to_tuple(left_path), y+1) # Get number of splits on Left path
            timelines += particle_cached(to_tuple(right_path), y+1) # Left path

        else:
            path = copy.deepcopy(manifold_map)
            path[y][beam] = "|"
            timelines += particle_cached(to_tuple(path), y+1)

    return timelines

with open("7/input.txt", "r") as inpt:
    # manifold = np.array([[ch for ch in line if ch != "\n"] for line in inpt.readlines()])
    manifold = [[ch for ch in line if ch != "\n"] for line in inpt.readlines()]
    manifold_copy = copy.deepcopy(manifold)    
    
    # manifold = [line.replace("\n", "") for line in inpt.readlines()]

print()
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

# solution_2 = particle(manifold_copy, 1)
solution_2 = particle_cached(to_tuple(manifold_copy), 1)
print(particle_cached.cache_info())

t = time.time() - st
print("\n", "=" * 30, sep="")
print(f"Part 1: {solution_1} - {solution_1 == 21}")
print(f"Part 2: {solution_2} - {solution_2 == 40}")
# print(solution)
print("=" * 30,  sep="")
print(f"t: {t:.4f} \n")

