import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
#Extractin first row
first_row = arr[0]
print("First row:", first_row)
#Extracting Last column
print("Last column:", arr[:, -1])
#Extracting 2x2 subarray from the center
subarray = arr[1:3, 1:3]
print("2x2 subarray from the center:", subarray)