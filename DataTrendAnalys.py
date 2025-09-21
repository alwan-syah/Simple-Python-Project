import pandas as pd  
import seaborn as sns  
import matplotlib.pyplot as plt  

#Load time-series data  
df_ta = pd.read_csv('Sales Data.csv', parse_dates=['Order Date'])  
df_ta.set_index('Order Date', inplace=True)

#Resample monthly & calculate total sales  
monthly_sales = df_ta['Sales'].resample('M').sum()

#Line Plot: Monthly trend  
plt.figure(figsize=(10, 5))  
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values)  
plt.title('Monthly Sales Trend')  
plt.xlabel('Month')  
plt.ylabel('Total Sales')  
plt.xticks(rotation=45)  
plt.tight_layout()  
plt.show()

#Add rolling average  
monthly_sales.rolling(3).mean().plot(label='3-Month Avg', linewidth=2)  
monthly_sales.plot(label='Actual', alpha=0.5)  
plt.legend()  
plt.title('Sales with Rolling Average')  
plt.tight_layout()  
plt.show()


# Try Modifying:
# - Use .resample('W') for weekly trends  
# - Add anomaly detection  
# - Group by Year or Quarter