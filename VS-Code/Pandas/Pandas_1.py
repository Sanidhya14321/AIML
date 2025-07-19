# Pandas Basics
# It is a powerful data manipulation library in Python for data analysis.
# It provides data structures like Series and DataFrame for efficient data handling.

# import pandas as pd
# s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
# print(s)

# import pandas as pd
# data ={"Name": ["Alice", "Bob", "Charlie", "David"],
#         "Age": [25, 30, 35, 40],
#         "City": ["New York", "Los Angeles", "Chicago", "Houston"]}
# df = pd.DataFrame(data)
# print(df)

# Data loading methods
# -Excel
# -CSV
# -JSON

# df.to_csv('data.csv', index=False)                                     # Save DataFrame to a CSV file
# df.to_excel('data.xlsx', index=False)                                  # Save DataFrame to an Excel
# df.to_json('data.json', orient='records', lines=True)                  # Save DataFrame to a JSON file
# df.to_html('data.html', index=False)                                   # Save DataFrame to an HTML file
# df.to_pickle('data.pkl')                                               # Save DataFrame to a pickle file
# df.to_sql('table_name', con=engine, if_exists='replace', index=False)  # Save DataFrame to SQL database

# DataFrame operations
# -Filtering
# -Sorting
# -Grouping
# -Aggregation

# -Viewing and indexing
# print(df.head())                  # Display the first few rows of the DataFrame
# print(df.tail())                  # Display the last few rows of the DataFrame
# print(df.shape)                   # Get the shape of the DataFrame (rows, columns)
# print(df.info())                  # Get a concise summary of the DataFrame
# print(df.describe())              # Get descriptive statistics of the DataFrame

# -Selecting and indexing
# print(df['Name'])                 # Select a single column
# print(df[['Name', 'Age']])        # Select multiple columns
# print(df.iloc[0])                 # Select the first row by index
# print(df.loc[0])                  # Select the first row by label
# print(df[df['Age'] > 30])         # Filter rows based on a condition
#print(df.loc[:, "Name"])           # Select all rows for the "Name" column
# print(df.iloc[0:2])               # Select the first two rows

