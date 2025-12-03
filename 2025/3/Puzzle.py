import re
import numpy as np
import time
import numpy as np

solution_1 = 0
solution_2 = 0

 
    
st = time.time()

with open("3/input.txt", "r") as inpt:
    banks = np.array([[int(y) for y in i] for i in re.findall(r"\d+", inpt.read())])


for bank in banks:
    jolt_index1 = np.argmax(bank)
    if jolt_index1 < len(bank) - 1:
        jolt_index2 = np.argmax(bank[jolt_index1 + 1:]) + jolt_index1 + 1
    elif jolt_index1 == len(bank) - 1:
        jolt_index2 = np.argmax(bank[:jolt_index1])

    max_joltage = int(f"{bank[min(jolt_index1, jolt_index2)]}{bank[max(jolt_index1, jolt_index2)]}")
    solution_1 += max_joltage
    
    # print(bank, end=" ")
    # print(f"{jolt_index1:2} - {jolt_index2:2} -> {max_joltage}")

t = time.time() - st

print("\n", "=" * 30, sep="")
print(f"Part 1: {solution_1} - {solution_1 == 17074}")
print(f"Part 2: {solution_2} - {solution_2 == 3121910778619}")
print("=" * 30,  sep="")
print(f"t: {t:.4f} \n")

