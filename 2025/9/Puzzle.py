import time
import networkx as nx
import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from shapely.geometry import box, Polygon

def GetKey(box_a, box_b):
    return frozenset((tuple(box_a), tuple(box_b)))

solution_1 = 0
solution_2 = 0

st = time.time()

instalation = np.loadtxt("9/input.txt", int, delimiter=",")

areas = {}
areas2 = {}

bounds = Polygon(instalation)

for P1 in instalation:
    for P2 in instalation:
        key = GetKey(P1, P2) # this is hashable AND order of elements doesn't matter
        if key in areas.keys() or np.array_equal(P1, P2):
            continue        
        
        rect = box(P1[0], P1[1], P2[0], P2[1])
        if bounds.contains(rect): # Valid rectangles for part 2    
            areas2[key] = np.prod(np.abs(P2 - P1, dtype=object) + 1)
        areas[key] = np.prod(np.abs(P2 - P1, dtype=object) + 1)
 
areas =  dict(sorted(areas.items(), key=lambda item: item[1]))

max_area = max(areas, key=areas.get)
max_area2 = max(areas2, key=areas.get)
sol_1 = np.array(tuple(max_area))
sol_2 = np.array(tuple(max_area2))
solution_1 = areas[max_area]
solution_2 = areas2[max_area2]

t = time.time() - st
print("\n", "=" * 30, sep="")
print(f"Part 1: {solution_1} - {solution_1 == 4758121828}")
print(f"Part 2: {solution_2} - {solution_2 == 40}")
print("=" * 30,  sep="")
print(f"t: {t:.4f} \n")
# plt.plot(range(len(areas)), areas.values())


fig, ax = plt.subplots(figsize=(10, 7))

for i in range(len(instalation)):
    index2 = (i+1) % len(instalation) # It loops back to 0 when i reaches end of array
    (p1, p2) = (instalation[i], instalation[index2]) 
    
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color = "black")

(x1, y1), (x2, y2) = sol_1
x0 = min(x1, x2)
y0 = min(y1, y2)
width  = abs(x1 - x2)
height = abs(y1 - y2)

ax.add_patch(patches.Rectangle((x0, y0), width, height, fill=None, color="red", linewidth=3))

(x1, y1), (x2, y2) = sol_2
x0 = min(x1, x2)
y0 = min(y1, y2)
width  = abs(x1 - x2)
height = abs(y1 - y2)

ax.add_patch(patches.Rectangle((x0, y0), width, height, fill=None, color="blue", linewidth=3))

instalation = instalation.transpose()
ax.scatter(instalation[0], instalation[1])
ax.invert_yaxis()
ax.grid()


plt.show()