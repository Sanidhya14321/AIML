# -Concatenation
# -Merging
# -Joining
# import pandas as pd
# Concatenation
# # Concatenating two DataFrames vertically
# df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
# df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
# df_concat = pd.concat([df1, df2], axis=0, ignore_index=True)
# print("Concatenated DataFrame:\n", df_concat)
# # Concatenating two DataFrames horizontally
# df3 = pd.DataFrame({'C': [9, 10], 'D': [11, 12]})
# df_concat_horizontal = pd.concat([df1, df3], axis=1)
# print("\nHorizontally Concatenated DataFrame:\n", df_concat_horizontal)

# Merging
# # Merging two DataFrames on a common column
# df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
# df2 = pd.DataFrame({'key': ['B', 'C', 'D'], 'value2': [4, 5, 6]})
# df_merged = pd.merge(df1, df2, on='key', how='right')
# print("\nMerged DataFrame:\n", df_merged)
# # Merging two DataFrames with different column names
# import pandas as pd
# df3 = pd.DataFrame({'key1': ['A', 'B', 'C'], 'value3': [7, 8, 9]})
# df4 = pd.DataFrame({'key2': ['B', 'C', 'D'], 'value4': [10, 11, 12]})
# df_merged_diff = pd.merge(df3, df4, left_on='key1', right_on='key2', how='inner')
# print("\nMerged DataFrame with different column names:\n", df_merged_diff)

# Joining
# # Joining two DataFrames on their indices
# import pandas as pd
# df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['a', 'b'])
# df2 = pd.DataFrame({'C': [5, 6], 'D': [7, 8]}, index=['b', 'c'])
# df_joined = df1.join(df2, how='outer')
# print("\nJoined DataFrame:\n", df_joined)