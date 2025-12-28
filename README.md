# Python Excel Sales Report Automation

This project automates the creation of a sales report PDF starting from an Excel file.
It is designed for small businesses or individuals who need to clean messy data and generate reports quickly and reliably.

---

## 🚀 What the script does

The script performs an end-to-end automation pipeline:

1. Reads sales data from an Excel file
2. Cleans and validates the data
3. Performs basic calculations
4. Generates a summary chart
5. Exports a professional PDF report

---

## 🧹 Data Cleaning Features

The script handles common real-world data issues:

- Removes rows with missing values
- Converts dates to proper datetime format
- Handles European decimal format (e.g. `49,99 → 49.99`)
- Removes invalid quantities (Quantity ≤ 0)
- Removes duplicate rows
- Calculates total sales per transaction

---

## 📊 Output

The script generates:

- `sales_by_category.png`
  A bar chart showing total sales by product category

- `sales_report.pdf`
  A clean PDF report containing:
  - Report title
  - Total sales amount
  - Number of valid transactions
  - Sales chart centered on the page

---

## 📁 Project Structure

python-excel-report-automation/
├── main.py
├── sales_data.xlsx
├── sales_by_category.png
├── sales_report.pdf
├── requirements.txt
└── README.md

---

## 🛠 Technologies Used

- Python 3
- pandas
- matplotlib
- reportlab
- openpyxl

---

## ▶️ How to run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Run the script
   python main.py

3. The PNG chart and PDF report will be generated in the project folder.

## 💡 Use Cases

- Monthly sales reporting
- Excel automation for small businesses
- Data cleaning and validation
- Automated report generation
- Replacing manual Excel workflows

## 📌 Notes

This project is intentionally simple and focused on reliability and clarity.
It demonstrates how Python can be used to automate repetitive business tasks and produce ready-to-share outputs.
