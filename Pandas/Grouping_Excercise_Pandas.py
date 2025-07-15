# #GROUP DATA BY A CATEGORICAL COLUMN AND CALCULATE MEAN

# import pandas as pd

# data = {
#     "Class": ["A", "B", "A", "B", "C", "C"],
#     "Score": [85, 90, 88, 72, 95, 80],
#     "Age": [15, 16, 15, 17, 16, 15],
# }

# df = pd.DataFrame(data)

# # print("Original DataFrame: \n")
# # print(df)

# # grouped = df.groupby("Class").mean()
# # print("\nGrouped DataFrame with mean scores and ages: \n")
# # print(grouped)


# #CALCULATE SUMMARY STATISTICS FOR GROUPED DATA

# stats1 = df.groupby("Class").agg({
#     "Score": ["mean", "max", "min"],
# })
# stats2 = df.groupby("Class").agg({
#     "Age": ["mean", "max", "min"]
# })
# print("\nSummary statistics for grouped data: \n")
# print(stats1)
# print("\nSummary statistics for grouped data (second calculation): \n")
# print(stats2)

#custom aggregation function to calculate the variance of each group
# def variance(x):
#     return x.var()
#GROUP DATA BY A CATEGORICAL COLUMN AND CALCULATE VARIANCE
# import pandas as pd
# data = {
#     "Class": ["A", "B", "A", "B", "C", "C"],
#     "Score": [85, 90, 88, 72, 95, 80],
#     "Age": [15, 16, 15, 17, 16, 15],
# }
# df = pd.DataFrame(data)
# grouped_variance = df.groupby("Class").agg({
#     "Score": variance,
#     "Age": variance
# })
# print("\nGrouped DataFrame with variance of scores and ages: \n")
# print(grouped_variance)
