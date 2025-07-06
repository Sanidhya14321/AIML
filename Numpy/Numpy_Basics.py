import numpy as np

#functions in numpy

#1. numpy.array() - Converts input into a numpy array.
#2. numpy.arange() - Creates an array with evenly spaced values within a range.
#3. numpy.linspace() - Creates an array of evenly spaced values over a specified interval.
#4. numpy.logspace() - Creates an array with values spaced evenly on a log scale.
#5. numpy.zeros() - Creates an array filled with zeros.
#6. numpy.ones() - Creates an array filled with ones.
#7. numpy.full() - Creates an array filled with a specified value.
#8. numpy.eye() - Creates a 2D identity matrix.
#9. numpy.reshape() - Changes the shape of an array without changing its data.
#10. numpy.resize() - Resizes an array and fills extra space if needed.
#11. numpy.transpose() - Transposes (swaps axes of) an array.
#12. numpy.swapaxes() - Swaps two specified axes.
#13. numpy.stack() - Stacks arrays along a new axis.
#14. numpy.concatenate() - Concatenates arrays along an existing axis.
#15. numpy.append() - Appends values to an array.
#16. numpy.insert() - Inserts values at a specified index.
#17. numpy.delete() - Deletes elements from an array.
#18. numpy.split() - Splits an array into multiple sub-arrays.
#19. numpy.hstack() - Stacks arrays horizontally (column-wise).
#20. numpy.vstack() - Stacks arrays vertically (row-wise).
#21. numpy.dstack() - Stacks arrays depth-wise (along the third axis).
#22. numpy.ravel() - Flattens an array into 1D.
#23. numpy.flatten() - Returns a copy of an array collapsed into 1D.
#24. numpy.ndim - Returns the number of dimensions of an array.
#25. numpy.shape - Returns the shape (dimensions) of an array.
#26. numpy.size - Returns the total number of elements.
#27. numpy.dtype - Returns the data type of an array.
#28. numpy.astype() - Casts an array to a specified type.
#29. numpy.random.rand() - Generates random numbers from a uniform distribution.
#30. numpy.random.randn() - Generates random numbers from a normal distribution.
#31. numpy.random.randint() - Generates random integers within a range.
#32. numpy.random.choice() - Selects random elements from a 1D array.
#33. numpy.random.shuffle() - Shuffles an array in-place.
#34. numpy.random.permutation() - Returns a shuffled version of an array.
#35. numpy.random.seed() - Sets the seed for random number generation.
#36. numpy.where() - Returns indices where a condition is true.
#37. numpy.nonzero() - Returns indices of non-zero elements.
#38. numpy.argwhere() - Returns indices of elements satisfying a condition.
#39. numpy.searchsorted() - Finds indices to maintain order.
#40. numpy.sort() - Sorts an array.
#41. numpy.argsort() - Returns the indices that would sort an array.
#42. numpy.partition() - Partially sorts an array.
#43. numpy.argpartition() - Returns indices for partial sorting.
#44. numpy.mean() - Computes the mean of elements.
#45. numpy.median() - Computes the median of elements.
#46. numpy.std() - Computes standard deviation.
#47. numpy.var() - Computes variance.
#48. numpy.ptp() - Computes the range (max - min).
#49. numpy.percentile() - Computes the nth percentile.
#50. numpy.sum() - Computes the sum of array elements.
#51. numpy.min() - Computes the minimum value.
#52. numpy.max() - Computes the maximum value.
#53. numpy.cumsum() - Cumulative sum.
#54. numpy.cumprod() - Cumulative product.
#55. numpy.unique() - Finds the unique elements.
#56. numpy.isin() - Tests whether elements are in another array.
#57. numpy.clip() - Limits values to a specified range.
#58. numpy.round() - Rounds array values.
#59. numpy.floor() - Rounds values down.
#60. numpy.ceil() - Rounds values up.
#61. numpy.trunc() - Truncates values to integer toward zero.
#62. numpy.meshgrid() - Creates coordinate matrices from vectors.
#63. numpy.indices() - Generates a grid of indices for an array shape.
#64. numpy.mgrid - Dense multidimensional "meshgrid".
#65. numpy.ogrid - Open grid (for broadcasting).
#66. numpy.histogram() - Computes a histogram of array data.
#67. numpy.histogram2d() - Computes a 2D histogram.
#68. numpy.histogramdd() - Computes an N-D histogram.
#69. numpy.polyfit() - Fits a polynomial to data.
#70. numpy.polyval() - Evaluates a polynomial.
#71. numpy.polyder() - Computes the derivative of a polynomial.
#72. numpy.polyint() - Computes the integral of a polynomial.
#73. numpy.poly1d() - Constructs a polynomial object.
#74. numpy.linalg.inv() - Computes the inverse of a matrix.
#75. numpy.linalg.det() - Computes the determinant of a matrix.
#76. numpy.linalg.eig() - Computes eigenvalues and eigenvectors.
#77. numpy.linalg.solve() - Solves a linear matrix equation.


# Most used NumPy functions

#1. numpy.array() - Converts input into a NumPy array.
#2. numpy.arange() - Creates an array with evenly spaced values within a specified range.
#3. numpy.linspace() - Creates an array of evenly spaced values over a specified interval.
#4. numpy.zeros() - Creates an array filled with zeros.
#5. numpy.ones() - Creates an array filled with ones.
#6. numpy.full() - Creates an array of a specified shape and fills it with a constant value.
#7. numpy.eye() - Creates a 2D identity matrix (ones on the diagonal, zeros elsewhere).
#8. numpy.reshape() - Reshapes an array without changing its data.
#9. numpy.ravel() - Flattens an array into 1D.
#10. numpy.flatten() - Returns a copy of the array collapsed into 1D.
#11. numpy.transpose() - Transposes (swaps axes of) an array.
#12. numpy.concatenate() - Concatenates arrays along an existing axis.
#13. numpy.vstack() - Stacks arrays vertically (row-wise).
#14. numpy.hstack() - Stacks arrays horizontally (column-wise).
#15. numpy.stack() - Stacks arrays along a new axis.
#16. numpy.split() - Splits an array into multiple sub-arrays.
#17. numpy.mean() - Computes the mean of array elements.
#18. numpy.median() - Computes the median of array elements.
#19. numpy.std() - Computes the standard deviation.
#20. numpy.var() - Computes the variance.
#21. numpy.sum() - Computes the total sum of array elements.
#22. numpy.min() - Finds the minimum value in the array.
#23. numpy.max() - Finds the maximum value in the array.
#24. numpy.sort() - Sorts the array.
#25. numpy.argsort() - Returns the indices that would sort the array.
#26. numpy.unique() - Returns the sorted unique elements of an array.
#27. numpy.where() - Returns indices where a condition is true.
#28. numpy.random.rand() - Generates random samples from a uniform distribution.
#29. numpy.random.randint() - Generates random integers within a specified range.
#30. numpy.random.seed() - Sets the seed for NumPy's random number generator for reproducibility.