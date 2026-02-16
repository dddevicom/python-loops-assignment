import numpy as np

# 1. Create NumPy array
temps_celsius = np.array([22, 25, 28, 24, 26])

# 2. Convert to Fahrenheit
temps_fahrenheit = temps_celsius * 1.8 + 32

# 3. Print both arrays
print(f"Celsius:{temps_celsius}")
print(f"Fahrenheit:{temps_fahrenheit}")

# 4. Calculate average Fahrenheit (rounded to 1 decimal)
average_fahrenheit = round(np.mean(temps_fahrenheit), 1)
print(f"Average Fahrenheit:{average_fahrenheit}")
