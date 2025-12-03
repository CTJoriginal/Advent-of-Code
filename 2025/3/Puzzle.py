import re
import time
import numpy as np

solution_1 = 0, solution_2 = 0

# Num batteries should be one less than actual number of digits in answer
def yoltage(bank, solution = [], num_batteries = 2):
    index = np.argmax(bank[:-num_batteries or None]) # usage of the "or None" -> arr[:-0] == [] vs arr[:None] == arr
    solution.append(bank[index])
    
    if num_batteries > 0:
        return yoltage(bank[index+1:], solution, num_batteries - 1)
    else:
        return int("".join(map(str, solution)))
    
st = time.time()
with open("3/input.txt", "r") as inpt:
    banks = np.array([[int(y) for y in i] for i in re.findall(r"\d+", inpt.read())])

for bank in banks:
    solution_1 += yoltage(bank, [], 1)
    solution_2 += yoltage(bank, [], 11)
    
t = time.time() - st

print("\n", "=" * 30, sep="")
print(f"Part 1: {solution_1} - {solution_1 == 17074}")
print(f"Part 2: {solution_2} - {solution_2 == 169512729575727}")
print("=" * 30,  sep="")
print(f"t: {t:.4f} \n")

