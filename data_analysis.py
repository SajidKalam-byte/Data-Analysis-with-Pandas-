import pandas as pd

# Load the CSV file
file_path = r'D:\sample.csv'  # Adjust the file path
data = pd.read_csv(file_path)

# 1. Display the first 5 rows
print("First 5 rows of the dataset:")
print(data.head())

# 2. Display the shape of the dataset
print("\nShape of the dataset (rows, columns):")
print(data.shape)

# 3. Display the data types of each column
print("\nData types of each column:")
print(data.dtypes)

# 4. Descriptive statistics of numerical columns
print("\nDescriptive statistics:")
print(data.describe())

# 5. Checking for duplicate rows
duplicates = data.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates}")

# 6. Count of unique values in a specific column (e.g., 'Name')
if 'Name' in data.columns:
    unique_names = data['Name'].nunique()
    print(f"\nNumber of unique names: {unique_names}")

# 7. Grouping and Aggregation (e.g., average Salary by Age)
if 'Age' in data.columns and 'Salary' in data.columns:
    avg_salary_by_age = data.groupby('Age')['Salary'].mean()
    print("\nAverage salary by age:")
    print(avg_salary_by_age)

# 8. Sorting the dataset by a column (e.g., 'Salary' in descending order)
if 'Salary' in data.columns:
    sorted_data = data.sort_values(by='Salary', ascending=False)
    print("\nTop 5 rows sorted by Salary (descending):")
    print(sorted_data.head())

# 9. Filtering data based on a condition (e.g., Salary > 50,000)
if 'Salary' in data.columns:
    high_salary = data[data['Salary'] > 50000]
    print(f"\nRows where Salary > 50,000 (Total: {high_salary.shape[0]}):")
    print(high_salary)

# 10. Exporting the filtered data to a new CSV file
output_path = r'D:\high_salary.csv'
high_salary.to_csv(output_path, index=False)
print(f"\nFiltered data saved to {output_path}")
