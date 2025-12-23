# pip install nltk
# pip install scikit-learn

from flask import Flask, request, jsonify
import re
import nltk
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from flask_cors import CORS

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

app = Flask(__name__)
CORS(app)  # Allow React frontend to talk to Flask

# Load the trained model and vectorizer
try:
    loaded_model = pickle.load(open("model.pkl", 'rb'))
    vector = pickle.load(open("vectorizer.pkl", 'rb'))
except Exception as e:
    print(f"Error loading model or vectorizer: {e}")
    exit(1)  # Exit if loading fails

lemmatizer = WordNetLemmatizer()
stpwrds = set(stopwords.words('english'))

# Preprocessing and prediction function
def fake_news_det(news):
    print("Original news:", news)  # Log the original news text
    review = re.sub(r'[^a-zA-Z\s]', '', news)  # Remove non-alphabetical characters
    review = review.lower()
    review = nltk.word_tokenize(review)
    corpus = [lemmatizer.lemmatize(word) for word in review if word not in stpwrds]

    input_data = [' '.join(corpus)]
    vectorized_input_data = vector.transform(input_data)

    # Get prediction probabilities
    prediction_proba = loaded_model.predict_proba(vectorized_input_data)
    print(f"Prediction probabilities: {prediction_proba}")  # Log probabilities
    return prediction_proba

@app.route('/')
def home():
    return "Welcome to Fake News Detection API!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        message = data.get('text')
        if not message:
            return jsonify({'error': 'No text provided'}), 400
        
        prob = fake_news_det(message)
        fake_prob = prob[0][0]  # Assuming class 0 = Fake, 1 = Real

        threshold = 0.9  # Set threshold (you can adjust between 0.6–0.7)

        if fake_prob > threshold:
            result = "Fake"
            confidence = fake_prob * 100
        else:
            result = "Real"
            # confidence = (1 - fake_prob) * 100
            confidence = (fake_prob) * 100

        return jsonify({
            'prediction': result,
            'confidence': f"{confidence:.2f}%"
        }), 200
    except Exception as e:
        print("Error during prediction:", str(e))
        return jsonify({'error': 'Something went wrong on server'}), 500

if __name__ == '__main__':
    app.run(debug=True)