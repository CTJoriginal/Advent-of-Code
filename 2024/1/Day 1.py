import numpy as np

inp = np.loadtxt("input.txt", dtype=int)
list1 = np.sort(inp[:, 0])
list2 = np.sort(inp[:, 1])

total_distance = np.sum([np.abs(var - list2[index]) for index, var in enumerate(list1)])

print("Solution 1:", total_distance)    

### Part 2 ###

counts = {}
# Count how many times number appears in second list and add them to dict
for i in list2:
    if i not in counts: 
        counts[i] = 0
    counts[i] += 1

# Sum all the scores, but only if curreent number from first list was recorded in second list
# Else similarity score gain is 0
similarity_score = np.sum([i * counts[i] for i in list1 if i in counts])

print("Solution 2:", similarity_score)    