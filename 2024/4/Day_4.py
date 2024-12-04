import numpy as np

def SearchXMAS(index, array, cols, rows, word = "XMAS"):
    directions = np.array([
        #X, Y
        [0, 1],  #N 
        [1, 0],  #E
        [0, -1], #S
        [-1, 0], #W
        [1, 1],  #NW
        [1, -1], #SE
        [-1, -1],#SW
        [-1, 1]])  #NW
        
    count = 0
    for direction in directions:
        Found = True
        for i in range(len(word)):
            sx, sy = index + i * direction

            if sx > cols - 1 or sy > rows - 1 or sx < 0 or sy < 0:
                Found = False
                break
            
            if array[sx][sy] != word[i]:
                Found = False
                break
            
            # If this passes, the word was matched!
        if Found:
            count += 1

    return count
        


data = open("2024\\4\\input.txt", "r").readlines()
data = np.array([[char for char in string if char != "\n"] for string in data])

rows, cols = data.shape

Sum = 0
for x in range(rows):
    for y in range(cols):
        if data[x, y] == "X":
            Sum += SearchXMAS(np.array([x, y]), data, cols, rows)

print("Part 1: ", Sum)


### PART 2 ###
# Find X-MAS instead of XMAS

def SearchX_MAS(index, array):
    mask = [['M', '.', 'S'],
            ['.', 'A', '.'],
            ['M', '.', 'S']]
    
    x, y = index

    element = np.array(array[x-1 : x+2, y-1: y+2]) # COPY SLICE OF ARRAY SO ORIGINAL IS NOT MODIFIED!
    element[0, 1] = "."
    element[1, 0] = "."
    element[2, 1] = "."
    element[1, 2] = "."

    for i in range(4):
        if np.array_equal(mask, element):
            return True
        else:
            mask = np.rot90(mask)

    return False


rows, cols = data.shape

Sum = 0
PaintedData = np.array(data)
for x in range(1, rows-1):
    for y in range(1, cols-1):
        Sum += SearchX_MAS(np.array([x, y]), data)
        
print("Part 2: ", Sum)