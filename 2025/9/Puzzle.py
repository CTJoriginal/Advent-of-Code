import time
import networkx as nx
import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Source: https://www.geeksforgeeks.org/dsa/flood-fill-algorithm/
def dfs(img, x, y, oldColor, newColor):
    if (x < 0 or x >= len(img) or
        y < 0 or y >= len(img[0]) or
        img[x][y] != oldColor):
        return

    # Update the color of the current pixel
    img[x][y] = newColor

    # Recursively visit all 4 connected neighbors
    dfs(img, x + 1, y, oldColor, newColor)
    dfs(img, x - 1, y, oldColor, newColor)
    dfs(img, x, y + 1, oldColor, newColor)
    dfs(img, x, y - 1, oldColor, newColor)

# Source: https://www.geeksforgeeks.org/dsa/flood-fill-algorithm/
def floodFill(img, sr, sc, newColor):
    if img[sr][sc] == newColor:
        return img

    oldColor = img[sr][sc]
    dfs(img, sr, sc, oldColor, newColor)

    return img

def GetKey(box_a, box_b):
    return frozenset((tuple(box_a), tuple(box_b)))

solution_1 = 0
solution_2 = 0

st = time.time()

instalation = np.loadtxt("9/input.txt", int, delimiter=",")

areas = {}

for P1 in instalation:
    for P2 in instalation:
        key = GetKey(P1, P2) # this is hashable AND order of elements doesn't matter
        if key in areas.keys() or np.array_equal(P1, P2):
            continue        

        areas[key] = np.prod(np.abs(P2 - P1, dtype=object) + 1)
 
areas =  dict(sorted(areas.items(), key=lambda item: item[1]))

max_area = max(areas, key=areas.get)
sol_1 = np.array(tuple(max_area))
solution_1 = areas[max_area]

t = time.time() - st
print("\n", "=" * 30, sep="")
print(f"Part 1: {solution_1} - {solution_1 == 4758121828}")
print(f"Part 2: {solution_2} - {solution_2 == 40}")
print("=" * 30,  sep="")
print(f"t: {t:.4f} \n")
# plt.plot(range(len(areas)), areas.values())


fig, ax = plt.subplots(1, 2, figsize=(10, 7))

# THIS USES 36 GiB of RAM AHHHHHHHHHHH
tilemap = np.zeros([np.max(instalation) + 2, np.max(instalation) + 2], dtype=int)

for i in range(len(instalation)):
    
    index2 = (i+1) % len(instalation) # It loops back to 0 when i reaches end of array
    (p1, p2) = (instalation[i], instalation[index2]) 
    
    ax[0].plot([p1[0], p2[0]], [p1[1], p2[1]], color = "black")
    
    if p1[0] == p2[0]:
        tilemap[min(p1[1], p2[1]):max(p1[1], p2[1])+1, p1[0]] = 1
    elif p1[1] == p2[1]:
        tilemap[p1[1], min(p1[0], p2[0]):max(p1[0], p2[0])+1] = 1

ys, xs = np.where(tilemap == 1)

tilemap = floodFill(tilemap, int(np.median(ys)), int(np.median(xs)), 1)

print(tilemap)

(x1, y1), (x2, y2) = sol_1
x0 = min(x1, x2)
y0 = min(y1, y2)
width  = abs(x1 - x2)
height = abs(y1 - y2)

ax[0].add_patch(patches.Rectangle((x0, y0), width, height, fill=None, color="red", linewidth=3))

instalation = instalation.transpose()
ax[0].scatter(instalation[0], instalation[1])
ax[0].invert_yaxis()
ax[0].grid()
ax[1].imshow(tilemap)
# ax[1].grid()
# ax[1].invert_yaxis()
rows, cols = tilemap.shape[:2]

ax[1].set_xticks(np.arange(cols))
ax[1].set_yticks(np.arange(rows))
ax[1].set_xticklabels(np.arange(cols))
ax[1].set_yticklabels(np.arange(rows))
ax[1].grid(color='black', linestyle='-', linewidth=0.00001)
ax[1].set_xticks(np.arange(-.5, cols, 1), minor=True)
ax[1].set_yticks(np.arange(-.5, rows, 1), minor=True)
ax[1].grid(which='minor', color='white', linestyle='-', linewidth=0.5)


plt.show()