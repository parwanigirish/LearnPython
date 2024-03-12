import numpy as np

# Creating arrays
arr1 = np.array([2, 4, 6])
arr2 = np.array([4, 5, 6])

# Array multiplication
result = np.multiply(arr1, arr2)
print("Array Multiplication:", result)

# Matrix multiplication
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
result = np.matmul(matrix1, matrix2)
print("Matrix Multiplication:\n", result)
