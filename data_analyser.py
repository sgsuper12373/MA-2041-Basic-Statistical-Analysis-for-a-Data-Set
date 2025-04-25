import pandas as pd

# Load the file
df = pd.read_csv("Imports_of_Major_Petrochemicals_Product_Wise_or_Group_Wise_2014-15_to_2021-22.csv")

# Clean column names (remove trailing spaces)
df.columns = [col.strip() for col in df.columns]

# Convert quantity and value columns to numeric
df["2021-22 QTY"] = pd.to_numeric(df["2021-22 QTY"], errors='coerce')
df["2021-22 VAL"] = pd.to_numeric(df["2021-22 VAL"], errors='coerce')

# Group by 'Group' and sum the quantity and value
grouped_df = df.groupby("Group")[["2021-22 QTY", "2021-22 VAL"]].sum().reset_index()

# Save to new CSV
grouped_df.to_csv("Grouped_Imports_by_Group_2021-22.csv", index=False)
