import numpy as np
# create an array with numbers 10 to 50
my_array = np.arange(10, 51)
print(my_array)

#find the maximum and minimum values in the array
max_value = np.max(my_array)
min_value = np.min(my_array)
print("Maximum value:", max_value)
print("Minimum value:", min_value)

#multiply the array by 3
my_array = my_array * 3
print("Array after multiplication by 3:", my_array)

