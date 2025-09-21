import pandas as pd

# Load CSV file
df = pd.read_csv('Sales data.csv')

# Drop duplicate rows
df = df.drop_duplicates()

# Fill missing values (example: fill empty 'Sales' with 0)
df['Sales'] = df['Sales'].fillna(0)

# Convert 'Date' column to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Remove rows with missing essential fields
df = df.dropna(subset=['City', 'Product'])

# Export cleaned data
df.to_csv('cleaned_data.csv', index=False)

# Try Modifying:  
# - Normalize column names  
# - Add logging to track issues  
# - Integrate with Excel writer