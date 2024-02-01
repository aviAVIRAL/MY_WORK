




import pandas as pd

# Create a sample CSV file
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 22, 28],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv('sample_data.csv', index=False)

# Read the CSV file into a new DataFrame
new_df = pd.read_csv('sample_data.csv')

# Display the original and new DataFrames
print("Original DataFrame:")
print(df)

print("\nDataFrame read from CSV:")
print(new_df)
