# Broadcasting in NumPy allows you to perform operations on arrays of different shapes and sizes without needing to explicitly reshape them.
# This is particularly useful for performing element-wise operations on arrays.
# - Dimension Compatibility: Arrays can be broadcast together if their dimensions are compatible or 1.
# - Rules of Broadcasting: The smaller array is "stretched" to match the shape of the larger array.

# import numpy as np
# # Example of broadcasting
# a = np.array([[1, 2, 3], [4, 5, 6]])
# b = np.array([10, 20, 30])
# # Broadcasting allows us to add a 1D array to a 2D array
# result = a + b
# print("Result of broadcasting addition:\n", result)

# Aggregation functions in NumPy are used to perform operations on arrays that reduce their dimensionality, such as summing or averaging elements.
# - Common Functions: `np.sum()`, `np.mean()`, `np.min()`, `np.max()`, `np.std()`
# - Axis Parameter: You can specify the axis along which to perform the operation.
# import numpy as np
# # Example of aggregation functions
# a = np.array([[1, 2, 3], [4, 5, 6]])

       # Sum of all elements
# total_sum = np.sum(a)
# print("Total sum of all elements:", total_sum)

       # Mean of all elements
# mean_value = np.mean(a)
# print("Mean value of all elements:", mean_value)

       # Minimum value in the array
# min_value = np.min(a)
# print("Minimum value in the array:", min_value)

       # Maximum value in the array
# max_value = np.max(a)
# print("Maximum value in the array:", max_value)

       # Standard deviation of all elements
# std_dev = np.std(a)
# print("Standard deviation of all elements:", std_dev)


# Boolean indexing in NumPy allows you to filter arrays based on conditions, enabling you to select elements that meet specific criteria.
# - Creating Boolean Masks: You can create a boolean mask by applying a condition to an array
# - Using Masks: You can use the boolean mask to index the original array and retrieve elements that satisfy the condition.

# boolean indexing for filtering elements in an array as even numbers
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# evens=arr[arr%2==0]
# print("Even numbers in the array:", evens)

# Random number generation in NumPy is used to create arrays filled with random numbers, which can be useful for simulations, testing, and statistical analysis.
# - Random Seed: Setting a random seed ensures reproducibility of random numbers.
# - Random Functions: NumPy provides various functions to generate random numbers, such as `np.random.rand()`, `np.random.randn()`, and `np.random.randint()`.

# import numpy as np
# random_array= np.random.rand(3, 4)  
# print("Random array with values between 0 and 1:\n", random_array)

# random_array2= np.random.randint(1,4, size=(3, 4))
# print("Random array with integer values between 1 and 10:\n", random_array2)

