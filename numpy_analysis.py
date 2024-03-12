import numpy as np

# Creating sample data
ages = np.array([25, 30, 35, 40, 45, 50, 55, 60, 65, 70])
heights = np.array([165, 170, 172, 175, 168, 180, 185, 178, 182, 190])

# Calculating mean and standard deviation
mean_age = np.mean(ages)
std_height = np.std(heights)

print("Mean Age:", mean_age)
print("Standard Deviation of Heights:", std_height)

# Finding values above a threshold
tall_people = heights[heights > 180]
print("People Taller than 180cm:", tall_people)