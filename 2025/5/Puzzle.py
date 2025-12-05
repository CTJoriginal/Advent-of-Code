import time
import re
import numpy as np

solution_1 = 0
solution_2 = np.array([])

st = time.time()

with open("5/input.txt", "r") as inpt:
    inpt = inpt.read()
    ranges = [(int(d1), int(d2)) for d1, d2 in re.findall(r"^(\d+)-(\d+)$", inpt, re.MULTILINE)]
    items = [int(d) for d in re.findall(r"^\d+$", inpt, re.MULTILINE)]


for item in items:
    for low, high in ranges:
        if item >= low and item <= high:
            solution_1 += 1
            break
        
for low, high in ranges:
    arr =  np.arange(low, high + 1, dtype=np.int64)
    print(arr)
    solution_2 = np.unique(np.concatenate((solution_2, arr)))

t = time.time() - st

print("\n", "=" * 30, sep="")
print(f"Part 1: {solution_1} - {solution_1 == 868}")
print(f"Part 2: {len(solution_2)} - {len(solution_2) == 14}")
print(np.sort(solution_2))
print("=" * 30,  sep="")
print(f"t: {t:.4f} \n")

