import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'Grouped_Imports_by_Group_All_Years.csv'  # Replace with your CSV file path
data = pd.read_csv(file_path)

# Display the first few rows of the data
print(data.head())

# Extract the years for quantities and values
quantity_years = [col.split()[0] for col in data.columns if 'QTY' in col]
value_years = [col.split()[0] for col in data.columns if 'VAL' in col]

# Plot the data for quantities
plt.figure(figsize=(12, 8))
for index, row in data.iterrows():
    group_name = row['Group']
    quantities = [row[f'{year} QTY'] for year in quantity_years]
    plt.plot(quantity_years, quantities, marker='o', label=group_name)

# Customize the plot for quantities
plt.xlabel('Year')
plt.ylabel('Quantity')
plt.title('Multi-Line Graph of Quantities by Group Over Years')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Place legend outside the plot
plt.grid(True)
plt.tight_layout()  # Adjust layout to fit everything
plt.show()

# Plot the data for values
plt.figure(figsize=(12, 8))
for index, row in data.iterrows():
    group_name = row['Group']
    values = [row[f'{year} VAL'] for year in value_years]
    plt.plot(value_years, values, marker='o', label=group_name)

# Customize the plot for values
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Multi-Line Graph of Values by Group Over Years')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Place legend outside the plot
plt.grid(True)
plt.tight_layout()  # Adjust layout to fit everything
plt.show()