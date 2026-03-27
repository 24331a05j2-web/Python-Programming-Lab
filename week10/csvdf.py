import pandas as pd
df = pd.read_csv('data.csv')

print("First 5 rows of the dataset:")
print(df.head())

print("\nLast 5 rows of the dataset:")
print(df.tail())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())