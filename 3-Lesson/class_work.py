# 1-task
import numpy as np

# 2-task
print('--- This is the 1D array ---')
array1 = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
print(array1, "\n")
# 3-task
print('--- This is extracting all the odd numbers ---')
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr, "\n")
extracted_array = arr[1::2]
print(extracted_array, "\n\n")

# 4-task
print("--- This is replacing all odd numbers with '-1' ---")
arr1 = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
print(arr1, "\n")
arr1[1::2] = -1
print(arr1, "\n\n")

# 5-task
print("--- Here is the 3x3 of all 'Trues ---'")
array_of_all_trues = np.array([[1, 1, 1],
                               [1, 1, 1],
                               [1, 1, 1]])
print(array_of_all_trues, "\n\n")
change_of_array = array_of_all_trues.astype(bool)
print(change_of_array, "\n")