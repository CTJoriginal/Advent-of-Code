import time
import numpy as np
import re
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

solution_1 = 0
solution_2 = 0

st = time.time()

with open("11/input.txt") as inpt:
    arr = []
    for start, ends in re.findall(r"^(\S+):\s*(.+)$", inpt.read(), re.MULTILINE):
        for e in ends.split(" "):
            arr.append([start, e])

G = nx.DiGraph()
G.add_edges_from(arr)

print("Compute part 1")
solution_1 = len(list(nx.all_simple_paths(G, "you", "out")))

print("Simplifying graph...")

start, p2, p3, end = "svr", "fft", "dac", "out"

a = set(nx.descendants(G, start)) | {start}
b = set(nx.ancestors(G, p2)) | {p2}
sg_svr2fft = G.subgraph(a & b)

a = set(nx.descendants(G, p2)) | {p2}
b = set(nx.ancestors(G, p3)) | {p3}
sg_fft2dac = G.subgraph(a & b)

a = set(nx.descendants(G, p3)) | {p3}
b = set(nx.ancestors(G, end)) | {end}
sg_dac2out = G.subgraph(a & b)

# G2 = nx.compose_all([sg_svr2fft, sg_fft2dac, sg_dac2out])

print("Finding paths...")

print("   Sg1")
paths1 = list(nx.all_simple_paths(sg_svr2fft, start, p2))
print("   Sg2")
paths2 = list(nx.all_simple_paths(sg_fft2dac, p2, p3))
print("   Sg3")
paths3 = list(nx.all_simple_paths(sg_dac2out, p3, end))

solution_2 = len(paths1) * len(paths2) * len(paths3)

time = time.time() - st

print("\n", "=" * 50, sep="")
print(f"Part 1: {solution_1} - {solution_1 == 7}")
print(f"Part 2: {solution_2} - {solution_2 == 85513235135}")
print("=" * 50,  sep="")
print(f"t: {time:.4f} \n")