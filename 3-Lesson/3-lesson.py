import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,0]])
arr1 = np.array([[[1,2,3], [4,5,6]], [[7,8,9],[10,11,12]]])

print(arr)
print(arr1)
print(arr[0,2])

# Dimensions of the array
print(arr.ndim)
print(arr1.ndim)

# Get the desired output
print(arr[0])
print(arr1[1])
print(arr[0]+arr[1])