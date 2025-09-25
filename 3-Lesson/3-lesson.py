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

arr2 = np.array([1.1, 2.1, 3.1])
newarr = arr2.astype('i')
print(newarr)
print(newarr.dtype)

x = arr.copy()
print(x)

arr3 = np.array([1,2,3,4,5,6,7])
print(arr[0:2,2])

print(arr.reshape(-1))

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
print(np.vstack((array1, array2)))
print(np.dstack((array1, array2)))

x = [1,2,3,4]
y = [4,5,6,7,9]