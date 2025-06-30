# main.py
import pandas as pd
import os
from cleaner import clean_data
from visualize_data import visualize_data
from report import generate_report

os.makedirs("reports", exist_ok=True)

# Load dataset
df = pd.read_csv("data/raw_data.csv")

# Clean dataset
df_cleaned, cleaning_log = clean_data(df)

# Visualize data
visualize_data(df_cleaned)

# Generate report
generate_report(df_cleaned, cleaning_log)

print("Pipeline completed successfully.")
