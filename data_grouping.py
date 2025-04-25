import pandas as pd

# Loading the file
df = pd.read_csv("Imports_of_Major_Petrochemicals_Product_Wise_or_Group_Wise_2014-15_to_2021-22.csv")

# Clean column names
df.columns = [col.strip() for col in df.columns]

# List of years
years = ["2014-15", "2015-16", "2016-17", "2017-18", "2018-19", "2019-20", "2020-21", "2021-22"]

# Convert all QTY and VAL columns to numeric
for year in years:
    df[f"{year} QTY"] = pd.to_numeric(df[f"{year} QTY"], errors='coerce')
    df[f"{year} VAL"] = pd.to_numeric(df[f"{year} VAL"], errors='coerce')

# Group by 'Group' and sum all years' quantities and values
qty_cols = [f"{year} QTY" for year in years]
val_cols = [f"{year} VAL" for year in years]
grouped_df = (df.groupby("Group")[qty_cols + val_cols].sum()/1000).reset_index()

#removing last row of csv file we are not using total import of major petrochemicals for analysis
grouped_df = grouped_df[grouped_df['Group'] != 'Total Import Of Major Petrochemicals']

# Save to new CSV
grouped_df.to_csv("Grouped_Imports_by_Group_All_Years.csv", index=False)
