import pandas as pd  
from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LinearRegression  
from sklearn.metrics import mean_squared_error  

# Load dataset  
df = pd.read_csv('house_data.csv')  # Example CSV with columns: area, bedrooms, location, price  

# Convert categorical data  
df = pd.get_dummies(df, columns=['location'], drop_first=True)

# Features & Target  
X = df.drop('price', axis=1)  
y = df['price']  

# Split data  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model  
model = LinearRegression()  
model.fit(X_train, y_train)

# Predict  
predictions = model.predict(X_test)  
print("MSE:", mean_squared_error(y_test, predictions))