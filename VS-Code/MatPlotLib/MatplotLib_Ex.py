# import matplotlib.pyplot as plt
# # Line Plot

# years = [2010, 2011, 2012, 2013]
# sales = [120, 140, 160, 180]
# plt.plot(years, sales, label="Sales Trend", color = "blue", marker="o")
# plt.title("Sales Trend Over Years")
# plt.xlabel("Years")
# plt.ylabel("Sales")
# plt.legend()
# plt.show()

# # Bar Plot
# import matplotlib.pyplot as plt
# import numpy as np
# years = [2010, 2011, 2012, 2013]
# sales = [120, 140, 160, 180]
# plt.bar(years, sales, label="Sales Trend", color = "blue")
# plt.title("Sales Trend Over Years")
# plt.xlabel("Years")
# plt.ylabel("Sales")
# plt.legend()
# plt.show()

#Scatter Plot

# import matplotlib.pyplot as plt

# hours_studied = [1, 2, 3, 4, 5]
# exam_scores = [55, 63, 72, 88, 98]
# plt.scatter(hours_studied, exam_scores, color = "red")
# plt.title("Study hours vs Exam Scores")
# plt.xlabel("Study Hours")
# plt.ylabel("Exam Scores")
# plt.show()

# # Create a Histogram with multiple datasets overlaid
# import matplotlib.pyplot as plt
# import numpy as np
# # Create a figure and a set of subplots
# fig, axs = plt.subplots(2, 2, figsize=(10, 8))
# # Create a histogram for the first dataset
# axs[0, 0].hist(np.random.randn(1000), bins=30, color='blue', alpha=0.7, label='Dataset 1')

# axs[0, 0].set_title("Histogram of Dataset 1")
# # Create a histogram for the second dataset
# axs[0, 1].hist(np.random.randn(1000), bins=30, color='green', alpha=0.7, label='Dataset 2')
# # Create a histogram for the third dataset
# axs[1, 0].hist(np.random.randn(1000), bins=30, color='red', alpha=0.7, label='Dataset 3')
# # Create a histogram for the fourth dataset
# axs[1, 1].hist(np.random.randn(1000), bins=30, color='yellow', alpha=0.7, label='Dataset 4')
# # Add a legend to the first subplot
# axs[0, 0].legend()
# # Show the plot
# plt.show()


