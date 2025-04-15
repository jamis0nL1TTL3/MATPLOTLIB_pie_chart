# Use Numpy to generate a random 2-dimensional numpy array with dimensions 5x5
# Print the array, then print the number from the 2nd row 3rd column
# Print the sum of all the elements in the array
# Print the mean of each row in the array
# Print the maximum value in each column of the array

import numpy as np

random_list = [np.random.randint(10, size=5) for _ in range (5)]
random_array = np.array(random_list)
row_means = np.mean(random_array, axis=1)
# axis = 1 is the row, axis = 0 is the column
column_max = np.max(random_array, axis=0)

print (random_array)

print (random_array [1,2])
# [:, ::-1] flips array (what was last becomes first, what was second to the last becomes second, etc.)
# row 0 = first row, row 1 = second row, etc.
# column 0 = first column, column 1 = second column, etc.
print (np.sum(random_array))
print (row_means)
print (column_max)
