# Handling missing values in a DataFrame using Pandas
# Methods to handle missing values in a DataFrame
# - Drop missing values
# - Fill missing values with a specific value
# - Interpolate missing values

# df = df.dropna()                                     # Drop rows with any NaN values
# df = df.dropna(axis=1)                               # Drop columns with any NaN values

# df["column_name"] = df["column_name"].fillna(value)  # Fill NaN values in a specific column
# df.fillna(method='ffill', inplace=True)  # Forward fill NaN values
# df.fillna(method='bfill', inplace=True)  # Backward fill NaN values

# df["column_name"] = df["column_name"].interpolate()  # Interpolate NaN values in a specific column
# df.interpolate(method='linear', inplace=True)  # Interpolate NaN values in the entire DataFrame
# df.interpolate(method='time', inplace=True)  # Interpolate NaN values based on time index
