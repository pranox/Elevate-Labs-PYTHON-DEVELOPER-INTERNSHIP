# Task 05 – Data Analysis on CSV Files

## 🚀 Objective
Analyze sales data from a CSV file using **Pandas** and visualize insights.

## 🔧 Features
- Load CSV data into Pandas DataFrame
- Perform basic analysis:
  - Total Sales by Region
  - Total Quantity by Product
  - Total Revenue (Quantity × Price)
- Generate bar charts for better visualization
- Output PDF attached with screenshots

## 📁 Files Included
- `Data_Analysis_task.ipynb` — Jupyter Notebook with code and analysis
- `sales_data.csv` — Sample sales dataset
- `output.pdf` — Contains analysis output and screenshots
- `README.md` — This file

## 🛠 Tech Stack
- Python 3
- Pandas
- Matplotlib / Seaborn (optional)
- Jupyter Notebook / Google Colab

## 📊 Dataset Structure
| Date       | Region | Product  | Quantity | Price |
|-------------|--------|----------|----------|-------|
| 2024-01-01 | North  | Pen      | 100      | 1.50  |
| 2024-01-02 | South  | Notebook | 150      | 2.50  |
| 2024-01-03 | East   | Pencil   | 200      | 0.50  |
| ...        | ...    | ...      | ...      | ...   |

## 📈 Analysis Performed
- Grouped data by **Region** to calculate total sales
- Grouped data by **Product** to calculate total quantity sold
- Calculated total revenue by multiplying `Quantity * Price`
- Created bar charts for visual insights

## ▶️ How to Run

### 1️⃣ Install Dependencies
```bash
pip install pandas
pip install matplotlib
```

### 2️⃣ Run the Notebook
- Open `Task5_Data_Analysis.ipynb` in **Jupyter Notebook** or **Google Colab**.
- Run all the cells to see the outputs and visualizations.

## ✅ Output
- Charts are displayed in the notebook.
- Screenshots and output are available in `output.pdf`.

## 📜 License
This project is submitted as part of the **Elevate Labs Python Developer Internship Task 5**.

---

