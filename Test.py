import numpy as np
import sys

a = np.array([1, 2, 3], dtype='int8')
b = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

# print matrix
print(a)

# get dimension
print("Dimension", a.ndim)

# Get Type/Size
print("Type", b.dtype, "Size", b.itemsize, "Bytes")

