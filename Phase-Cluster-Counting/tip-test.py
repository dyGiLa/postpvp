import numpy as np

# Suppose we want a 3D array of shape (2, 3, 4)
i_max, j_max, k_max = 2, 3, 4

# Create a 1D array
array_1D = np.arange(i_max * j_max * k_max)

# Convert to 3D using reshape
array_3D = array_1D.reshape((i_max, j_max, k_max))

# Access an element using 3D indices
i, j, k = 1, 2, 3
index_1D = i * (j_max * k_max) + j * k_max + k

print(f"array_1D[{index_1D}] = {array_1D[index_1D]}")
print(f"array_3D[{i}, {j}, {k}] = {array_3D[i, j, k]}")