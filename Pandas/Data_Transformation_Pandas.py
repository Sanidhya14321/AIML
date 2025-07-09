# -Renaming Columns
# -Changing Data Types
# -Creating or Modifying Columns

# df = df.rename(columns={'old_name': 'new_name'})  # Rename a specific column
# df = df.rename(columns=lambda x: x.strip().lower())  # Rename all columns to lowercase and strip whitespace

# df['column_name'] = df['column_name'].astype('int')  # Change data type of a specific column
# df['column_name'] = pd.to_datetime(df['column_name'])  # Convert a column to datetime

# df['new_column'] = df['column1'] + df['column2']  # Create a new column based on existing columns
# df['new_column'] = df['column_name'].apply(lambda x: x * 2)  # Modify a column using a function