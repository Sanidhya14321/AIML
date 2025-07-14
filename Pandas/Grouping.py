# grouped = df.groupby('column_name')

# for name, group in grouped:
#     print(f"\nGroup: {name}")
#     print(group)
    
# grouped_mean = grouped.mean()

# grouped_sum = grouped.sum()

# df.groupby("category_column")["numeric_column"].mean()
# df.groupby("category_column").agg({"numeric_column": ["mean", "sum", "min", "max"]})

# pivot = df.pivot_table(index='category_column', values='numeric_column', aggfunc='mean')

# def range_func(x):
#     return x.max() - x.min()

# df.groupby("category_column")["numeric_column"].agg(range_func)

# df.groupby("category_column").agg(
#     {"numeric_column": ["mean", "sum", "min", "max"],}
# )
