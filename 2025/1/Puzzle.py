import re

dial = 50
dial_numbers = 99 + 1

num_zeroes_p1 = 0
num_zeroes_p2 = 0

with open("1/input.txt", "r") as inpt:
    instructions = [[-1 if match[0] == "L" else 1, int(match[1])] for match in re.findall(r"(L|R)(\d+)", inpt.read())]

for direction, distance in instructions:
    prev_position = dial
    rollover = False
    
    if distance > dial_numbers: # Handle multiple rotations of knob in same instruction
        num_zeroes_p2 += distance // dial_numbers
        distance = distance % dial_numbers
    
    dial += direction * distance # Move dial
    
    if dial > dial_numbers - 1:        
        dial = dial - dial_numbers; # Handle rollover
        rollover = True
        
    elif dial < 0:                
        dial = dial_numbers + dial; # Handle rollover
        rollover = True
    
    # Part 1
    if dial == 0: 
        num_zeroes_p1 += 1        
    
    # Part 2
    if rollover and dial != 0 and prev_position != 0 or dial == 0:
        num_zeroes_p2 += 1


print("\n", "=" * 50, sep="")
print(f"Part 1: {num_zeroes_p1}")
print(f"Part 2: {num_zeroes_p2}")
print("=" * 50,  sep="")
    