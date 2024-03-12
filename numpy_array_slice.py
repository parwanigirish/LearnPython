import numpy as np

# Creating an array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Reshaping the array
reshaped_arr = arr.reshape(3, 3)
print("Reshaped Array:\n", reshaped_arr)

# Slicing the array
sliced_arr = reshaped_arr[0:2, 1:]
print("Sliced Array:\n", sliced_arr)

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
reshaped_arr = arr.reshape(2,8)
print("\n")
print(reshaped_arr)

reshaped_arr = arr.reshape(4,4)
print("\n")
print(reshaped_arr)