import re
import time

t = time.time()

memory = open("2024\\3\\input.txt", "r").read()


# Regex returns in form:
# ('2', '55')
muls = re.findall(r"mul\((\d+),(\d+)\)", memory)

result1 = sum([int(x) * int(y) for x, y in muls]) 
print("Solution 1: ", result1)

print(f"It took: {time.time()-t} ms")
t = time.time()
### PART 2 ###

# Regex returns in form:
# [('2', '4', '', ''), 
# ('', '', '', "don't()"), 
# ('', '', 'do()', '')]

muls = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", memory)
enabled = True
result2 = 0

for x, y, En, Dis in muls:
    if En: 
        enabled = True
        continue
    if Dis: 
        enabled = False
        continue
    
    if enabled:
        result2 += int(x) * int(y)

print("Solution 2: ", result2)
print(f"It took: {time.time()-t} ms")