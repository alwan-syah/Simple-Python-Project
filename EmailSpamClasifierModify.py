import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
from collections import Counter
import streamlit as st

# --- Load dataset ---
df_es = pd.read_csv('spam.csv', encoding='latin-1')[['Category', 'Message']]
df_es.columns = ['label', 'text']
df_es['label'] = df_es['label'].map({'ham': 0, 'spam': 1})

# --- Split data ---
X_train, X_test, y_train, y_test = train_test_split(
    df_es['text'], df_es['label'], test_size=0.2, random_state=42
)

# --- Vectorize text ---
vectorizer = TfidfVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# --- Train Naive Bayes ---
nb_model = MultinomialNB()
nb_model.fit(X_train_vec, y_train)
nb_pred = nb_model.predict(X_test_vec)

print("Naive Bayes")
print(confusion_matrix(y_test, nb_pred))
print(classification_report(y_test, nb_pred))

# --- Train SVM ---
svm_model = LinearSVC()
svm_model.fit(X_train_vec, y_train)
svm_pred = svm_model.predict(X_test_vec)

print("\nSVM")
print(confusion_matrix(y_test, svm_pred))
print(classification_report(y_test, svm_pred))

# --- Train Logistic Regression ---
lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train_vec, y_train)
lr_pred = lr_model.predict(X_test_vec)

print("\nLogistic Regression")
print(confusion_matrix(y_test, lr_pred))
print(classification_report(y_test, lr_pred))

# --- Visualize most frequent spam words ---
spam_texts = " ".join(df_es[df_es['label'] == 1]['text'].tolist()).lower()
words = [w for w in spam_texts.split() if len(w) > 3]  # hapus kata terlalu pendek
counter = Counter(words)
common_words = counter.most_common(20)

# Plot
plt.figure(figsize=(10,5))
plt.bar([w for w, _ in common_words], [c for _, c in common_words])
plt.title("Most Frequent Spam Words")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Streamlit App ---
def run_app():
    st.title("📧 Spam Detector")
    st.write("Masukkan teks email untuk cek apakah spam atau tidak")

    user_input = st.text_area("Email Text")
    model_choice = st.selectbox("Pilih Model", ["Naive Bayes", "SVM", "Logistic Regression"])

    if st.button("Predict"):
        vec_input = vectorizer.transform([user_input])
        if model_choice == "Naive Bayes":
            pred = nb_model.predict(vec_input)[0]
        elif model_choice == "SVM":
            pred = svm_model.predict(vec_input)[0]
        else:
            pred = lr_model.predict(vec_input)[0]

        label = "🚫 SPAM" if pred == 1 else "✅ HAM (Not Spam)"
        st.subheader(f"Hasil Prediksi: {label}")

# Jalankan di terminal dengan: streamlit run nama_file.py
