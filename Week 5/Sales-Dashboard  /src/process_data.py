def calculate_total_sales(df):
    return df['Total Revenue'].sum()

def sales_by_region(df):
    return df.groupby('Region')['Total Revenue'].sum()
