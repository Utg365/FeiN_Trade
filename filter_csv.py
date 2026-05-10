import pandas as pd
from pathlib import Path

# Put your CSV file path here
input_file = r"C:\Users\Acer\Downloads\2026_05_07.csv"

# Read CSV
df = pd.read_csv(input_file)

# Column mapping
column_mapping = {
    "symbol": "Symbol",
    "open": "Open",
    "high": "High",
    "low": "Low",
    "close": "Close",
    "percent_change": "Diff %",
    "volume": "Vol",
    "turn_over": "Turnover"
}

# Create filtered dataframe
filtered_df = pd.DataFrame()

for new_name, old_name in column_mapping.items():
    if old_name in df.columns:
        filtered_df[new_name] = df[old_name]

# Get date from file name automatically
file_name = Path(input_file).stem
formatted_date = file_name.replace("_", "-")

# Add extra columns
filtered_df["date"] = formatted_date
filtered_df["sector"] = ""

# Reorder columns
filtered_df = filtered_df[
    ["symbol", "date", "open", "high", "low", "close",
     "percent_change", "volume", "turn_over", "sector"]
]

# Save new CSV
output_file = Path(input_file).with_name(f"filtered_{file_name}.csv")
filtered_df.to_csv(output_file, index=False)

print("Filtered file saved at:")
print(output_file)
