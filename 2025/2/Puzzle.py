import re
import numpy as np
import time

solution_1 = 0
solution_2 = 0

def SequenceDetector(num):
    arr = str(num)
    kernel = arr[:len(arr) // 2] # Pick first half of array
    result = re.findall(f"{kernel}", arr) # match repetitions of a kernel
    if len(arr) % 2 == 0 and len(result) * len(kernel) == len(arr):
        return True
    return False

def SequenceDetector2(num):
    arr = str(num)
    for i in range(len(arr) // 2 + 1):
        kernel = arr[0:i]
        result = re.findall(f"{kernel}", arr)
        if len(result) * len(kernel) == len(arr):
            return True


def SequenceDetectorOpt(num):
    arr = str(num)
    result = re.match(r"^(.*)\1+$", arr) # This matches all strings that are composed only of repeating characters
    # ^ $ match must be from beginning to end
    # (.*) Match any charatcers of any length
    # \1+ match all repetitions of this group
    if result != None and arr == result[0]: # if regex captures entire string, then it must be invalid
        return True


st = time.time()

with open("2/input.txt", "r") as inpt:
    instructions = [[int(i[0]), int(i[1])] for i in re.findall(r"(\d+)-(\d+)", inpt.read())]

for start, end in instructions:
    for i in range(start, end + 1):
        if SequenceDetector(i):
            # print(f"{i} - [{start} - {end}]")
            solution_1 += i
        if SequenceDetectorOpt(i):
            # print(f"{i} - [{start} - {end}]")
            solution_2 += i

time = time.time() - st

print("\n", "=" * 50, sep="")
print(f"Part 1: {solution_1} - {solution_1 == 64215794229}")
print(f"Part 2: {solution_2} - {solution_2 == 85513235135}")
print("=" * 50,  sep="")
print(f"t: {time:.4f} \n")

