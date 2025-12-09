import time
import networkx as nx
import numpy as np

def GetKey(box_a, box_b):
    return frozenset((tuple(box_a), tuple(box_b)))

solution_1 = 0
solution_2 = 0

st = time.time()

instalation = np.loadtxt("8/input.txt", int, delimiter=",")
nodes = {tuple(n): i for i, n in enumerate(instalation)}  # mapping node index --> name

distances = {}

# Compute distance between all pairs of boxes
for box_a in instalation:
    for box_b in instalation:
        # key = GetKey(box_a, box_b) # this is hashable AND order of elements doesn't matter
        key = frozenset((nodes[tuple(box_a)], nodes[tuple(box_b)])) # this is hashable AND order of elements doesn't matter
        if key in distances.keys() or np.array_equal(box_a, box_b):
            continue
                
        distances[key] = np.linalg.norm(box_a - box_b)

distances =  dict(sorted(distances.items(), key=lambda item: item[1]))
keys = list(distances.keys())

# for i in range(10):
#     k = keys[i]

# print(distances)
# print(distances.keys())



graph = np.zeros((len(nodes),len(nodes)))

for i in range(10):
    box_a, box_b = keys[i]
    graph[box_a][box_b] = 1
    graph[box_b][box_a] = 1

G = nx.from_numpy_array(graph)

subgraphs = sorted([len(G.subgraph(c).copy()) for c in nx.connected_components(G)], reverse=True)
solution_2 = np.prod(subgraphs[:3])

t = time.time() - st
print("\n", "=" * 30, sep="")
print(f"Part 1: {solution_1} - {solution_1 == 21}")
print(f"Part 2: {solution_2} - {solution_2 == 40}")
print("=" * 30,  sep="")
print(f"t: {t:.4f} \n")
