import numpy as np
a = np.arange(15).reshape(3, 5)

# Display array and its properties
print("Array a:\n", a)
print("Shape of a:", a.shape)
print("Number of dimensions of a:", a.ndim)
print("Data type of a elements:", a.dtype.name)
print("Size of each element (bytes):", a.itemsize)
print("Total number of elements:", a.size)
print("Type of a:", type(a))

# Create a 1-D array
b = np.array([6, 7, 8])
print("\nArray b:", b)
print("Type of b:", type(b))
