# report.py
from datetime import datetime
import os

def generate_report(df, log, output_name="report"):
    os.makedirs("reports", exist_ok=True)
    stats = df.describe().to_string()
    report = f"Timestamp: {datetime.now()}\n\n{stats}\n\nLog:\n{''.join(log)}"

    with open(f"reports/{output_name}.txt", "w") as txt_file:
        txt_file.write(report)
    df.describe().to_csv(f"reports/{output_name}.csv")

if __name__ == "__main__":
    import pandas as pd
    df = pd.DataFrame({
        "Age": [25, 28, 30, 22],
        "Score": [88, 92, 85, 90]
    })
    log = ["Sample log entry for report generation"]
    generate_report(df, log)
    print("Report generated.")
