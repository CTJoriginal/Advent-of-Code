import numpy as np

with open("2024\\9\\input.txt", "r") as file:
    data = [int(num) for num in file.read()]

fileArray = []

index = 0
freeSpace = False

for block in data:
    for cnt in range(block):
        if freeSpace:
            fileArray.append(None)
        else:
            fileArray.append(index)
    
    if not freeSpace:
        index += 1
    
    freeSpace = not freeSpace


fileArrayP1 = fileArray.copy()

index = -1
while True:
    index += 1

    if fileArrayP1[index] != None:
        if index == len(fileArrayP1)-2:
            break
        continue
    
    while True:
        fileIndex = fileArrayP1.pop()
        if fileIndex != None:
            break
    
    if index >= len(fileArrayP1)-1:
        fileArrayP1.append(fileIndex)
        break
        
    fileArrayP1[index] = fileIndex
    
    

fileString = "".join(str(x) if x is not None else "." for x in fileArrayP1)
print(fileString)
print("0099811188827773336446555566")

checksum = 0
for z, y in enumerate(fileArrayP1):
    checksum += z * y

print("Part 1:", checksum)




