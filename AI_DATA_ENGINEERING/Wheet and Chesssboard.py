# Wheat and Chessboard

import numpy as np
import matplotlib.pyplot as plt

# Function to calculate grains on an n x m chessboard
def calculate_wheat(n, m):
    indices_of_squares = np.arange(n * m).astype(np.uint64)
    board_ndarray = 2 ** indices_of_squares
    return board_ndarray.reshape(n, m)

# Calculate for an 8x8 chessboard
chessboard = calculate_wheat(8, 8)

# Total number of grains
total_grains = np.sum(chessboard)
print("Total number of grains on an 8x8 chessboard: {}".format(total_grains))

# Average of each column
average_columns = np.mean(chessboard, axis=0)

# Visualization of average grains in each column
plt.xlabel("Column")
plt.ylabel("Number")
plt.title("Number in Each Column")
plt.bar(np.arange(1, 9), average_columns)
plt.show()

# Wheat count heatmap
plt.xlabel("Column")
plt.ylabel("Row")
plt.title("Heatmap")
plt.pcolor(chessboard)
plt.colorbar()
plt.show()

# Calculate grains in the first half and second half
first_half = chessboard[0:4, :]
second_half = chessboard[4:8, :]
grains_first_half = np.sum(first_half)
grains_second_half = np.sum(second_half)

print("Grains in the first half: {}".format(grains_first_half))
print("Grains in the second half: {}".format(grains_second_half))
print("Product of grains in both halves: {}".format(grains_first_half * grains_second_half))

# Comparison of calculation times
%timeit calculate_wheat(8, 8)
