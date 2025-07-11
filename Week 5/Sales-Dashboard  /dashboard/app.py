# dashboard/app.py

import dash
from dash import html, dcc
import plotly.express as px
import requests
import pandas as pd

# Backend API endpoints
API_BASE = 'http://127.0.0.1:5000'  # Flask must be running!

# 1️⃣ Get total sales
total_sales_res = requests.get(f'{API_BASE}/total-sales')
total_sales = total_sales_res.json()['Total Sales']

# 2️⃣ Get sales by region
region_res = requests.get(f'{API_BASE}/sales-by-region')
region_data = pd.DataFrame(region_res.json())

# 3️⃣ Get sales by product
product_res = requests.get(f'{API_BASE}/sales-by-product')
product_data = pd.DataFrame(product_res.json())

# Create charts
region_fig = px.bar(
    region_data,
    x='Region',
    y='Total Revenue',
    title='Sales by Region',
    labels={'Total Revenue': 'Revenue ($)'}
)

product_fig = px.pie(
    product_data,
    names='Product',
    values='Total Revenue',
    title='Sales by Product'
)

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('📊 Real-Time Sales Dashboard', style={'textAlign': 'center'}),
    html.H2(f'Total Sales: ${total_sales:,.2f}', style={'textAlign': 'center', 'color': 'green'}),

    html.Div([
        dcc.Graph(figure=region_fig),
        dcc.Graph(figure=product_fig)
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
