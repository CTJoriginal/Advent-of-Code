import numpy as np
import os


# Map difference between all elements of report
def ComputeDmap(report):
    return np.array([report[i+1] - report[i] for i in range(len(report) -1)])

def CheckSafe(difference_map):
    return (np.all(difference_map > 0) or np.all(difference_map < 0)) and (np.all(np.abs(difference_map) <= 3))

data = open("2024\\2\\input.txt", "r").readlines()

safe_count = 0
for line in data: # For each line
    report = np.fromstring(line, sep=' ') # Convert to np array
    difference_map = ComputeDmap(report)
    # Criteria: 
    # - All values are either ascending or descending
    # - Difference must be at most 3 and at least 1

    if CheckSafe(difference_map):
        safe_count += 1

print("Solution 1: ", safe_count)

### PART 2 ###

safe_count = 0
for line in data: # For each line
    org_report = np.fromstring(line, sep=' ') # Convert to np array
    
    # Same criteria as part 1, but one value that's off can be ignored
    for i in range(len(org_report)):
        report = np.delete(org_report, i)
        difference_map = ComputeDmap(report)
        
        if CheckSafe(difference_map):
            safe_count += 1
            break

print("Solution 2: ", safe_count)