# CS 162 QUIZ
# Use NUMPY to create a 3 by 3 array with the provided numbers: 241, 33, 41 - 444, 22, 10 - 342, 122, 315
# Print out the data values (total)
# Print out the data at location row 1, column 2 in the array
# Print the sum of the third rows columns

import numpy as np

three_list = [[241, 33, 41], [444, 22, 10], [342, 122, 315]]
three_array = np.array(three_list)

row_sum = np.sum(three_array[2])

print ("Array:")
print (three_array)
print ("First row, Second column:")
print (three_array [0,1])
print ("Third rows sum:")
print (row_sum)


