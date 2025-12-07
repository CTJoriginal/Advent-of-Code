import time
import re
from functools import reduce
import numpy as np

solution_1 = 0
solution_2 = 0

st = time.time()

def cephalopod_math(scroll, operations):
    # Todays new thing: yield operator makes entire finction into an array constructor 
    # Output of this function is generator that can be converted to array using list(). This eliminates need for internal accumulating array
    for i, line in enumerate(scroll):
        if operations[i] == "+":
            yield np.sum(line, dtype=object)
        elif operations[i] == "*":
            yield np.prod(line, dtype=object) 

with open("6/input.txt", "r") as inpt:
    inpt = inpt.readlines()
    # Part 1
    numbers = np.array([[int(num) for num in re.findall(r"\d+", line)] for line in inpt[:-1]]).transpose()
    operations = np.array(re.findall(r"[+*]", inpt[-1]))
    # Part 2
    ctp_numbers = np.array([[char for char in line if char != "\n"] for line in inpt[:-1]], object).transpose()

# Part 2 prep
cephalopod_numbers = []
arr = [] # Temporary array to accumulate each collumn of numbers

for line in ctp_numbers: # Build array of centipede numbers
    merge = "".join(line).strip()

    if merge.isdigit():
        arr.append(int(merge))
    else:
        cephalopod_numbers.append(arr)
        arr = []
if arr:
    cephalopod_numbers.append(arr)

# Solve
solution_1 = sum(cephalopod_math(numbers, operations))
solution_2 = sum(cephalopod_math(cephalopod_numbers, operations))
t = time.time() - st

print("\n", "=" * 30, sep="")
print(f"Part 1: {solution_1} - {solution_1 == 6171290547579}")
print(f"Part 2: {solution_2} - {solution_2 == 8811937976367}")
# print(solution)
print("=" * 30,  sep="")
print(f"t: {t:.4f} \n")

