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
