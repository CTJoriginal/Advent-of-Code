import re

with open("1/input.txt", "r") as inpt:
    instructions = re.findall(r"(L|R)(\d+)", inpt.read())

safe = 50
safe_numbers = 99

num_zeroes_p1 = 0
num_zeroes_p2 = 0

print(safe)

for i in instructions:
    prev_safe = safe
    
    direction = -1 if i[0] == "L" else 1
    distance = int(i[1])
    
    if distance > (safe_numbers + 1):
        num_zeroes_p2 += distance // (safe_numbers + 1)
        distance = distance % (safe_numbers + 1)
    
    safe += direction * distance
    
    if safe > safe_numbers:        
        safe = safe - (safe_numbers + 1); # Handle rollover
        
        if safe != 0 and prev_safe != 0:
            num_zeroes_p2 += 1
        
    elif safe < 0:                
        safe = (safe_numbers + 1) + safe; # Handle rollover

        if safe != 0 and prev_safe != 0:
            num_zeroes_p2 += 1
    
    if safe == 0:
        num_zeroes_p1 += 1
        
    if safe == 0:
        num_zeroes_p2 += 1
    
print(f"Part 1: {num_zeroes_p1}")
print(f"Part 2: {num_zeroes_p2}")
    