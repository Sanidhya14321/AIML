# Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy.
# It provides an object-oriented API for embedding plots into applications that use general-purpose GUI toolkits.
# Matplotlib can be used in Python scripts, the Python and IPython shells (via the command line or a terminal),
# Jupyter notebooks, web application servers, and four graphical user interface toolkits.
# It is often used for data visualization in scientific computing, data analysis, and machine learning.
# Matplotlib supports various types of plots, including line plots, scatter plots, bar charts,
# histograms, box plots, and more. It also supports various customization options, such as colors,
# line styles, markers, and annotations. Matplotlib is widely used in the scientific and engineering communities
# for its flexibility and ease of use, making it a popular choice for creating high-quality visualizations of data.

# Example of using Matplotlib to create a simple line plot
# import matplotlib.pyplot as plt

# # Sample data
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

# # Create a line plot
# plt.plot(x, y)

# # Add labels and title
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Sample Line Plot')

# # Show the plot
# plt.show()

# # BAR CHART
# import matplotlib.pyplot as plt
# import numpy as np
# # Sample data
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([2, 3, 5, 7, 11])
# # Create a bar chart
# plt.bar(x, y)
# # Add labels and title
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Sample Bar Chart')
# # Show the plot
# plt.show()

# # Histogram
# import matplotlib.pyplot as plt
# import numpy as np
# # Sample data
# x = [1,2,2,3,3,3,3,4,4,4]
# # Create a histogram
# plt.hist(x, bins=30, density=True, alpha=0.6, color='green')
# # Add labels and title
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Sample Histogram')
# # Show the plot
# plt.show()

# # Scatter Plot
# import matplotlib.pyplot as plt
# import numpy as np
# # Sample data
# x = np.random.randint(1,20,100)
# y = np.random.randint(1,20,100)
# # Create a scatter plot
# plt.scatter(x, y)
# # Add labels and title
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Sample Scatter Plot')
# # Show the plot
# plt.show()

