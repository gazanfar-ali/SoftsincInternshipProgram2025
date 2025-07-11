# 📊 Real-Time Sales Dashboard

Welcome to our **Softsinc Internship 2025 Week 5 Team Project**!  
This project is a simple, real-time sales analytics dashboard built with **Python**, **Flask**, **Dash**, and **Plotly**.

---

## 🚀 Project Goal

The goal is to build a web dashboard that:
- Loads sales data from a file.
- Provides a backend REST API for live analytics.
- Shows interactive charts for sales by region and product.
- Updates dynamically to help make quick business decisions.

---

## 📂 Project Structure

📁 data/
├── sales_data.txt # Sample sales data
├── schema.md # Explains data columns

📁 src/
├── data_loader.py # Loads data
├── process_data.py # Processes data (grouping, totals)
├── api.py # Flask backend
├── init.py # Marks src as a package

📁 dashboard/
├── app.py # Dash web app

📄 requirements.txt # Python dependencies
📄 README.md # This file

yaml
Copy
Edit

---

## 🧩 How to Run

1️⃣ **Clone the repo**

```bash
git clone https://github.com/YOUR_USERNAME/sales-dashboard.git
cd sales-dashboard
2️⃣ Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the backend API

bash
Copy
Edit
python src/api.py
The API will be live at http://127.0.0.1:5000

4️⃣ Run the dashboard

Open a second terminal, then:

bash
Copy
Edit
python dashboard/app.py
The dashboard will open at http://127.0.0.1:8050

📈 API Endpoints
Route	Description
/	Home page
/total-sales	Returns total sales revenue
/sales-by-region	Returns revenue grouped by region
/sales-by-product	Returns revenue grouped by product

📦 Dependencies
Below are the libraries used in this project:

Library	Why It’s Needed	Version Example
Flask	Runs the backend REST API that serves the sales data	3.0.0
pandas	Loads, cleans, and processes the sales data files	2.2.2
dash	Builds the interactive dashboard web app	2.17.0
plotly	Provides interactive charts used by Dash	5.22.0
requests	Lets the dashboard fetch data live from the Flask API	2.31.0

✨ Team
Team Name: Real-Time Insights Squad

Members:

Gazanfar Ali — Python Developer

Arooj Aslam — Data Scientist

Bilal Ahmed — Data Visualization Engineer

Sara Khan — Team Lead
