import pandas as pd  
from sklearn.model_selection import train_test_split  
from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.naive_bayes import MultinomialNB  
from sklearn.metrics import classification_report, confusion_matrix  

# Load dataset  
df_es = pd.read_csv('spam.csv', encoding='latin-1')[['Category', 'Message']]  
df_es.columns = ['label', 'text']  

# Convert labels to binary  
df_es['label'] = df_es['label'].map({'ham': 0, 'spam': 1})

# Split data  
X_train, X_test, y_train, y_test = train_test_split(df_es['text'], df_es['label'], test_size=0.2, random_state=42)

# Vectorize text  
vectorizer = TfidfVectorizer(stop_words='english')  
X_train_vec = vectorizer.fit_transform(X_train)  
X_test_vec = vectorizer.transform(X_test)

# Train model  
model = MultinomialNB()  
model.fit(X_train_vec, y_train)

# Predict & Evaluate
y_pred = model.predict(X_test_vec)  
print(confusion_matrix(y_test, y_pred))  
print(classification_report(y_test, y_pred))

# Try Modifying:  
# - Use SVM or Logistic Regression  
# - Visualize most frequent spam words  
# - Build a Streamlit app to input your own email text