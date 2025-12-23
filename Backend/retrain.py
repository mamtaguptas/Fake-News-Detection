# retrain_model.py

import pandas as pd
import nltk
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.calibration import CalibratedClassifierCV
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Load your true and fake news datasets
true_news = pd.read_csv('True.csv')   # <<== your file name
fake_news = pd.read_csv('Fake.csv')   # <<== your file name

# Assuming your datasets have a "text" column
true_news['label'] = 1  # Real news
fake_news['label'] = 0  # Fake news

# Combine the two datasets
data = pd.concat([true_news, fake_news], axis=0).reset_index(drop=True)

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# Apply preprocessing
data['text'] = data['text'].apply(preprocess_text)

# Split data
X = data['text']
y = data['label']
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
xv_train = vectorizer.fit_transform(x_train)
xv_test = vectorizer.transform(x_test)

# Random Forest with Calibration
base_rfc = RandomForestClassifier(random_state=0)
RFC = CalibratedClassifierCV(base_rfc, method='isotonic', cv=5)
RFC.fit(xv_train, y_train)

# Save the model and vectorizer
pickle.dump(RFC, open('model.pkl', 'wb'))
pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))

print("✅ Model and Vectorizer retrained and saved successfully!")
