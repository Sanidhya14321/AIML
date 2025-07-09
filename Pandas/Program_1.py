import numpy as np
import pandas as pd

# Create a DataFrame with random data
data = {
    "Name": ["Alice", "Bob", np.nan, "David"],
    "Age": [25, np.nan, 35, 40],
    "Score": [88.5, 92.0, np.nan, 90.5]
}

df= pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"]=df["Score"].interpolate()
print("\nDataFrame after filling missing values:")
print(df)

df=df.rename(columns={"Name": "Full Name", "Score": "Test Score"})
print("\nDataFrame after renaming columns:")
print(df)