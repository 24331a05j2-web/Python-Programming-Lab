import pandas as pd

df = pd.read_csv('data.csv')

print("Original Data:\n")
print(df)

sorted_age = df.sort_values(by='Age')
print("\nSorted by Age (Ascending):\n")
print(sorted_age)

sorted_salary = df.sort_values(by='Salary', ascending=False)
print("\nSorted by Salary (Descending):\n")
print(sorted_salary)

sorted_multi = df.sort_values(by=['Department', 'Salary'])
print("\nSorted by Department and Salary:\n")
print(sorted_multi)

print("\nFirst 5 rows:\n")
print(df[:5])

print("\nRows from index 2 to 6:\n")
print(df[2:7])

print("\nSelecting Name and Salary columns:\n")
print(df[['Name', 'Salary']])

print("\nUsing loc (rows 1 to 4, specific columns):\n")
print(df.loc[1:4, ['Name', 'Department', 'Salary']])

print("\nUsing iloc (rows 0 to 3, columns 0 to 2):\n")
print(df.iloc[0:4, 0:3])