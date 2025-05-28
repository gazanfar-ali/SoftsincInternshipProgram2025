import os
import pandas as pd
from datetime import datetime

# --- Task 1 ---
def analyze_csv(file_path):
    df = pd.read_csv(file_path)
    missing_rows = df[df.isnull().any(axis=1)]
    unique_counts = df.nunique()
    return df, missing_rows, unique_counts

# --- Task 2 ---
def write_summary_report(file_path, df, missing_rows, unique_counts):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_path = file_path.replace('.csv', '_summary_report.txt')
    
    with open(report_path, 'w') as f:
        f.write(f"Report generated on: {timestamp}\n\n")
        f.write("--- Missing Values Rows ---\n")
        f.write(missing_rows.to_string(index=False))
        f.write("\n\n--- Unique Entry Count Per Column ---\n")
        f.write(unique_counts.to_string())

    print(f"Summary report written to: {report_path}")

# --- Challenge ---
def summarize_logs(directory):
    error_summary = {}
    for file in os.listdir(directory):
        if file.endswith(".log") or file.endswith(".txt"):
            path = os.path.join(directory, file)
            with open(path, 'r') as f:
                for line in f:
                    if "error" in line.lower():
                        error_summary[file] = error_summary.get(file, 0) + 1

    # Write error summary report
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_name = f"error_report_{timestamp}.txt"
    with open(os.path.join(directory, report_name), 'w') as f:
        f.write("Error Summary Report\n")
        f.write(f"Generated on: {timestamp}\n\n")
        for file, count in error_summary.items():
            f.write(f"{file}: {count} errors\n")

    print(f"Log error report saved as: {report_name}")

# Example Usage
if __name__ == "__main__":
    # Replace with actual paths when testing
    csv_file = "sample_data.csv"
    logs_dir = "./logs"

    if os.path.exists(csv_file):
        df, missing, unique = analyze_csv(csv_file)
        write_summary_report(csv_file, df, missing, unique)

    if os.path.isdir(logs_dir):
        summarize_logs(logs_dir)