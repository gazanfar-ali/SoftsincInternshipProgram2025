# report.py
from datetime import datetime

def generate_report(df, log, output_name="report"):
    stats = df.describe().to_string()
    report = f"Timestamp: {datetime.now()}\n\n{stats}\n\nLog:\n{''.join(log)}"

    with open(f"reports/{output_name}.txt", "w") as txt_file:
        txt_file.write(report)
    df.describe().to_csv(f"reports/{output_name}.csv")
