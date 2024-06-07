import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create a small dataset
data = {
    'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'Store': ['Store A', 'Store B', 'Store A', 'Store B', 'Store A', 'Store B', 'Store A', 'Store B', 'Store A', 'Store B'],
    'Product': ['Product 1', 'Product 2', 'Product 1', 'Product 2', 'Product 1', 'Product 2', 'Product 1', 'Product 2', 'Product 1', 'Product 2'],
    'Sales': [150, 200, 160, 210, 170, 220, 180, 230, 190, 240],
    'Quantity': [10, 15, 12, 18, 14, 20, 16, 22, 18, 24]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Check for missing values
print(df.isnull().sum())

# Display the data types
print(df.dtypes)

# Display basic statistics
print(df.describe())

# Display the first few rows
print(df.head())

# Plotting distributions
plt.figure(figsize=(10, 6))
sns.histplot(df['Sales'], bins=5, kde=True)
plt.title('Distribution of Sales')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

# Sales over time
plt.figure(figsize=(14, 7))
sns.lineplot(x='Date', y='Sales', hue='Store', data=df, marker='o')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

# Sales by Store
sales_by_store = df.groupby('Store')['Sales'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(x='Store', y='Sales', data=sales_by_store)
plt.title('Total Sales by Store')
plt.xlabel('Store')
plt.ylabel('Total Sales')
plt.show()

# Sales by Product
sales_by_product = df.groupby('Product')['Sales'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(x='Product', y='Sales', data=sales_by_product)
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()

summary = """
Key Findings:
1. Sales show an increasing trend over the period.
2. Store B has higher total sales compared to Store A.
3. Product 2 is slightly more popular in terms of sales compared to Product 1.

Recommendations:
1. Consider increasing inventory for Store B and Product 2.
2. Investigate reasons for lower sales in Store A and take corrective actions.
"""

print(summary)
