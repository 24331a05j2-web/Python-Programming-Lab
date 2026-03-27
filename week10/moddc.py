import pandas as pd
import numpy as np
df = pd.read_csv('data.csv')
print("Original Data:\n")
print(df)
df['Bonus'] = df['Salary'] * 0.10
df.rename(columns={'Dept': 'Department'}, inplace=True)
df.loc[df['Department'] == 'IT', 'Salary'] *= 1.05
df.drop(columns=['Experience'], inplace=True)
print("\nMissing Values:\n")
print(df.isnull().sum())
print("\nCleaned & Modified Data:\n")
print(df)
df.to_csv('cleaned_data.csv', index=False)