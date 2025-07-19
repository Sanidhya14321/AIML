import numpy as np

# arr = np.array([1,2,3,4,5,6,7,8,9])
# reshaped=arr.reshape(3, 3)
# print("Original Array:\n",arr)
# print("Reshaped Array:\n",reshaped)

# arr=np.array([1,2,3])
# expanded=arr[:,np.newaxis]
# print("Original Array:\n", arr)
# print("Expanded Array:\n", expanded)

# arr=np.array([4,16,25,36,49,64,81])
# sqrt_arr=np.sqrt(arr)
# print("Original Array:\n", arr)
# print("Square Root Array:\n", sqrt_arr)

# 4x4 matrix and calculate the sum of its rows and columns
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
# row_sum = np.sum(arr, axis=1)
# col_sum = np.sum(arr, axis=0)
# print("Original Array:\n", arr)
# print("Sum of Rows:\n", row_sum)
# print("Sum of Columns:\n", col_sum)

# Program to normalize an array(scaling values to a range of 0 to 1)
# arr= np.array([10, 20, 30, 40, 50])
# min_val = np.min(arr)
# max_val = np.max(arr)
# normalized_arr = (arr - min_val) / (max_val - min_val)
# print("Original Array:\n", arr)
# print("Normalized Array:\n", normalized_arr)

#genearate a random 3x3 matrix and calculate its minimum, maximum, and mean values
# arr= np.random.rand(3, 3)
# min_val = np.min(arr)
# max_val = np.max(arr)
# mean_val = np.mean(arr)
# print("Random 3x3 Matrix:\n", arr)
# print("Minimum Value:", min_val)
# print("Maximum Value:", max_val)
# print("Mean Value:", mean_val)

# Program to create a 2D array and transpose it
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# transposed_arr = arr.T
# print("Original Array:\n", arr)
# print("Transposed Array:\n", transposed_arr)

# Generate and filter a random dataset 
# dataset = np.random.randint(50, 100, size=(10, 5))
# print("Original Dataset:\n", dataset)
# filtered_dataset = dataset[dataset[:, 0] > 90]
# print("Filtered Dataset (First Column > 90):\n", filtered_dataset)
# mean_values = np.mean(filtered_dataset, axis=0)
# print("Mean Values of Each Column in Filtered Dataset:\n", mean_values)

# Program to create a 3d array and calculate the sum along a specific axis
# arr = np.random.randint(1,10, size=(3,3))
# sum_along_x_axis = np.sum(arr, axis=0)
# sum_along_y_axis = np.sum(arr, axis=1)
# print("Original 3D Array:\n", arr)
# print("Sum along axis 0:\n", sum_along_x_axis, "\nSum along axis 1:\n", sum_along_y_axis)

