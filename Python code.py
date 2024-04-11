import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('Employee dataframe.csv')

# Display the dataframe
print(df)

# Plot the data
df.plot(x='Performance Indicator', y='Employee ID', kind='scatter')
plt.show()

# Remove commas and convert to float
df['Salary (USD)'] = df['Salary (USD)'].str.replace(',', '').astype(float)
df['Increment (USD)'] = df['Increment (USD)'].str.replace(',', '').astype(float)

# Calculate total expenses
total_expenses = df[['Salary (USD)', 'Increment (USD)']].sum().sum()

# Get the income of the company
income = float(input("Enter the income of the company: "))

# Calculate profit
profit = income - total_expenses

# Print the results
print(f"Total expenses on increment and salary: {total_expenses:,.2f}")
print(f"Profit: {profit:,.2f}")

# Calculate average salary and increment
average_salary = df['Salary (USD)'].mean()
average_increment = df['Increment (USD)'].mean()

print(f"Average Salary (USD): {average_salary:,.2f}")
print(f"Average Increment (USD): {average_increment:,.2f}")

# Function to display basic statistics
def display_stats(df):
    print("\nData Statistics:")
    print(df.describe())

display_stats(df)
