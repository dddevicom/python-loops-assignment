import numpy as np
""" Task-2 my approch"""
# Creating the array of test scores
scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

# Getting required values Printing results using f-strings

print(f"Shape: {scores.shape}")
print(f"total_elements: {scores.size}" )
print(f"Highest score:{np.max(scores)}" )
print(f"Lowest score:{np.min(scores)}" )
print(f"Range: {np.max(scores) - np.min(scores)}")


#Task-2
# Creating the array of test scores
scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

# Getting required values
shape = scores.shape
total_elements = scores.size
highest_score = np.max(scores)
lowest_score = np.min(scores)
range_value = highest_score - lowest_score

# Printing results using f-strings
print(f"Shape: {shape}")
print(f"Total elements: {total_elements}")
print(f"Highest score: {highest_score}")
print(f"Lowest score: {lowest_score}")
print(f"Range: {range_value}")
