import time
import numpy as np
import re
import pulp


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
        
## LOGIC
print("Computing...")

from collections import deque

def bfs(machine):
    queue = deque([(np.zeros(len(machine.lights), int), 0)]) # state
    visited = set()
    
    while queue:
        curr, depth = queue.popleft()
        visited.add(tuple(curr))
        
        for but in machine.buttons:
            new_panel = np.bitwise_xor(curr, but)
            
            if np.array_equal(new_panel, machine.lights):
                # print(visited)
                return depth+1
            
            if tuple(new_panel) not in visited: # Check that node was not yet visited
                queue.append((new_panel, depth + 1))


    print(f"Solution not found for machine {machine.lights}")
    return 0

# for machine in machines:
#     solution_1.append(bfs(machine))

for machine in machines:
    model = pulp.LpProblem("Yoltages", pulp.LpMinimize)
    variables = [pulp.LpVariable(f"button_{i}", 0, cat="Integer") for i in range(len(machine.buttons))] # Variables that we optimise for

    model += pulp.lpSum(variables), "Presses" # Solution we are searching for (minimal sum of variables)
    
    for i in range(len(machine.yoltages)):
        print(i)
     #  constraint = pulp.lpSum(   x_vars[j] for j in range(m)                    if i in buttons[j])            
        constraint = pulp.lpSum(variables[j] for j in range(len(machine.buttons)) if i in machine.buttons[j])
        model += constraint == machine.yoltages[i], f"Sum {i}"
    
    model.solve()
    if pulp.LpStatus[model.status] == "Optimal":
        solution_2 += sum(int(pulp.value(var)) for var in variables)
    else: 
        print("SOLUTION NOT FOUND!")
    print( sum(int(pulp.value(var)) for var in variables))
    
    
time = time.time() - st

print("\n", "=" * 50, sep="")
print(f"Part 1: {sum(solution_1)} - {np.sum(solution_1) == 7}")
print(f"Part 2: {solution_2} - {solution_2 == 85513235135}")
print("=" * 50,  sep="")
print(f"t: {time:.4f} \n")