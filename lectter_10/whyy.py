import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
print(df)

average_age = df["age"].mean()
print(f"Average age: {average_age}")  # Output: Average age: 30.0

flipped_df = df.iloc[::-1]
print(flipped_df)  # Output: DataFrame with rows in reverse order

df['salary'] = [70000, 80000, 90000]
print(df)  # Output: DataFrame with an additional 'salary' column