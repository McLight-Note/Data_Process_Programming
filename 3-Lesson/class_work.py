# 1-task
import numpy as np

# 2-task
print('--- This is the 1D array ---')
array1 = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
print(array1, "\n")

# 3-task
print('--- This is extracting all the odd numbers ---')
arr = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
extracted_array = arr[1::2]
print(extracted_array, "\n")

# 4-task
print("--- This is replacing all odd numbers with '-1' ---")
arr1 = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
arr1[1::2] = -1
print(arr1, "\n")

# 5-task
print("--- Here is the 3x3 of all 'Trues'")
