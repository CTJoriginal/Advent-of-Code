import numpy as np
def Search(index, array, cols, rows, paintData):
    mask = [['M', '.', 'S'],
            ['.', 'A', '.'],
            ['M', '.', 'S']]
    
    x, y = index

    element = np.array(array[x-1 : x+2, y-1: y+2])
    element[0, 1] = "."
    element[1, 0] = "."
    element[2, 1] = "."
    element[1, 2] = "."

    print(element)


    for i in range(5):
        if np.array_equal(mask, element):
            paintData[x, y] =     "■"
            paintData[x-1, y-1] = "■"
            paintData[x+1, y+1] = "■"
            paintData[x-1, y+1] = "■"
            paintData[x+1, y-1] = "■"

            return True, paintData
        else:
            mask = np.rot90(mask)

    return False, paintData

data = open("TestInput.txt", "r").readlines()
data = np.array([[char for char in string if char != "\n"] for string in data])
print(data)

rows, cols = data.shape



Sum = 0
PaintedData = np.array(data)
for x in range(rows):
    for y in range(cols):
        if data[x, y] == "A":
            res, PaintedData = Search(np.array([x, y]), data, cols, rows, PaintedData)
            Sum += res
            print(x, y)

            print("   " + " ".join([str(i) for i in range(cols)]))
            # Print each row with its index
            # for i, row in enumerate(PaintedData):
            #     print(f"{i}  " + " ".join(row)) 
            # print()      
            # print()      


print("Part 2: ", Sum)
print(data)

# Print column indices
print("   " + " ".join([str(i) for i in range(cols)]))
# Print each row with its index
for i, row in enumerate(PaintedData):
    print(f"{i}  " + " ".join(row))