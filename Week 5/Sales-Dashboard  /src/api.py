# src/api.py

from flask import Flask, jsonify
from data_loader import load_data
from process_data import calculate_total_sales, sales_by_region, sales_by_product

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Sales Dashboard API</h1><p>Use /total-sales, /sales-by-region, /sales-by-product</p>"

@app.route('/total-sales')
def total_sales():
    df = load_data()
    total = calculate_total_sales(df)
    return jsonify({'Total Sales': total})

@app.route('/sales-by-region')
def region_sales():
    df = load_data()
    region_df = sales_by_region(df)
    result = region_df.to_dict(orient='records')
    return jsonify(result)

@app.route('/sales-by-product')
def product_sales():
    df = load_data()
    product_df = sales_by_product(df)
    result = product_df.to_dict(orient='records')
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
