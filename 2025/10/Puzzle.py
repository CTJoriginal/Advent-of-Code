import time
import numpy as np
import re

solution_1 = []
solution_2 = 0

st = time.time()

class Machine():
    def __init__(self):    
        self.lights = []
        self.buttons = []
        self.yoltages = []

    def __repr__(self):
        return f"L: {self.lights} \nB: {np.array(self.buttons)} \nY: {self.yoltages} \n ---------------"
    
pattern = re.compile(r"^\[([.#]+)\]\s*((?:\([^()]+\)\s*)+)\{([^}]+)\}$")
pattern_buttons = re.compile(r"\(([^()]+)\)")
pattern_digits = re.compile(r"\d+")

with open("10/input.txt") as inpt:
    machines = []
    for line in inpt.readlines():
        match = pattern.match(line.strip()).groups()
        machine = Machine()
        
        machine.lights = np.fromiter(((ch == "#") for ch in match[0]), int)
        for but in pattern_buttons.findall(match[1].strip()):
            arr = np.zeros(len(match[0]), dtype=int)
            arr[np.fromiter((int(n) for n in pattern_digits.findall(but)), int)] = 1
            machine.buttons.append(arr)
        
        machine.yoltages = np.fromiter((int(n) for n in pattern_digits.findall(match[2])), int)
        machines.append(machine)

def findCombo(machine, presses, max_presses, lights):
    for button in machine.buttons:
        new_lights = np.bitwise_xor(button, lights)
        if np.array_equal(machine.lights, new_lights):
            return presses
        if presses < max_presses:
            findCombo(machine, presses + 1, max_presses, new_lights)
             
    return -1
        
## LOGIC
print("Computing...")
for machine in machines:
    candidates = []
    for button in machine.buttons:
        res = findCombo(machine, 1, 10, np.zeros(len(machine.lights), dtype = int))
        if res > 0:
            candidates.append(res)
            break
    
    if candidates:
        solution_1.append(min(candidates))
    else:
        print(f"SOLUTION NOT FOND FOR MACHINE {machine.lights}")

time = time.time() - st

print("\n", "=" * 50, sep="")
print(f"Part 1: {solution_1} - {np.sum(solution_1) == 7}")
print(f"Part 2: {solution_2} - {solution_2 == 85513235135}")
print("=" * 50,  sep="")
print(f"t: {time:.4f} \n")

