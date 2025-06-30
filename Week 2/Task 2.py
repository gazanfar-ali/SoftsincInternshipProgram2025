import pandas as pd

def clean_data(df):
    log = []
    missing = df.isnull().sum()
    log.append(f"Missing values:\n{missing}\n")

    df.fillna(method='ffill', inplace=True)
    log.append("Filled missing values with forward fill\n")

    for col in df.columns:
        if 'date' in col.lower():
            df[col] = pd.to_datetime(df[col], errors='coerce')
            log.append(f"Converted {col} to datetime\n")

    return df, log
