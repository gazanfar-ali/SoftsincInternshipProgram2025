from flask import Flask, jsonify
from data_loader import load_data
from process_data import calculate_total_sales

app = Flask(__name__)

@app.route('/total-sales')
def total_sales():
    df = load_data('data/sales_data.csv')
    total = calculate_total_sales(df)
    return jsonify({'total_sales': total})

if __name__ == '__main__':
    app.run(debug=True)
