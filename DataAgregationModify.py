import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv('cleaned_data.csv')

# --- Filter data by year (contoh: hanya tahun 2023) ---
# Pastikan ada kolom 'Year' di dataset
df_filtered = df[df['Year'] == 2023]

# --- Aggregasi dengan .agg() untuk banyak metrik ---
# Total dan rata-rata sales per City
region_sales = df_filtered.groupby('City').agg(
    total_sales=('Sales', 'sum'),
    avg_sales=('Sales', 'mean'),
    max_sales=('Sales', 'max'),
    min_sales=('Sales', 'min')
).reset_index()

# Aggregasi produk: total dan rata-rata sales
product_summary = df_filtered.groupby('Product').agg(
    total_sales=('Sales', 'sum'),
    avg_sales=('Sales', 'mean')
).reset_index()

# Group by multiple columns (City + Product)
summary = df_filtered.groupby(['City', 'Product']).agg(
    total_sales=('Sales', 'sum')
).reset_index()

# --- Export to Excel ---
with pd.ExcelWriter('aggregated_report.xlsx', engine='openpyxl') as writer:
    region_sales.to_excel(writer, index=False, sheet_name='By City')
    product_summary.to_excel(writer, index=False, sheet_name='By Product')
    summary.to_excel(writer, index=False, sheet_name='City_Product')

# --- Visualisasi dengan Matplotlib ---
# 1. Bar chart: Total sales per City
plt.figure(figsize=(8,5))
plt.bar(region_sales['City'], region_sales['total_sales'])
plt.title('Total Sales by City (2023)')
plt.xlabel('City')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Bar chart: Total sales per Product
plt.figure(figsize=(8,5))
plt.bar(product_summary['Product'], product_summary['total_sales'], color='orange')
plt.title('Total Sales by Product (2023)')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
