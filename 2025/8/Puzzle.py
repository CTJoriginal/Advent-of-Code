import time
import networkx as nx
import numpy as np


solution_1 = 0
solution_2 = 0

st = time.time()

instalation = np.loadtxt("8/input.txt", int, delimiter=",")
nodes = {tuple(n): i for i, n in enumerate(instalation)}  # mapping node index --> name

distances = {}

G = nx.Graph()

for box in instalation:
    G.add_node(tuple(box))

# nx.draw(G)
# plt.show()

# Compute distance between all pairs of boxes
for box_a in instalation:
    for box_b in instalation:
        key = frozenset((tuple(box_a), tuple(box_b))) # this is hashable AND order of elements doesn't matter
        if key in distances.keys() or np.array_equal(box_a, box_b):
            continue

        distances[key] = np.linalg.norm(box_a - box_b)

distances = dict(sorted(distances.items(), key=lambda item: item[1]))
keys = list(distances.keys())

for i, pair in enumerate(keys):
    box_a, box_b = pair
    G.add_edge(box_a, box_b)
    
    if i == 999: # Part 1
        subgraphs = sorted([len(G.subgraph(c).copy()) for c in nx.connected_components(G)], reverse=True)
        solution_1 = np.prod(subgraphs[:3], dtype=object)
        
    if i % 1000 == 0:
        print(f"Progress: {i}")
    
    if nx.number_connected_components(G) == 1: # Part 2
        solution_2 = box_a[0] * box_b[0]
        break
    
t = time.time() - st
print("\n", "=" * 30, sep="")
print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")
print("=" * 30,  sep="")
print(f"t: {t:.4f} \n")
