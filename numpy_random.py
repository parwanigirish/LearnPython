import numpy as np

# Generating random numbers
random_nums = np.random.rand(15)  # 5 random numbers between 0 and 1
print("Random Numbers:", random_nums)

# Generating random integers
random_ints = np.random.randint(1, 11, size=10)  # 10 random integers between 1 and 10
print("Random Integers:", random_ints)

random_ints = np.random.randint(1, 1000, size=10)  # 10 random integers between 1 and 10
print("Random Integers:", random_ints)