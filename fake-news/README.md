# 📰 Fake News Detection System

This project is a **Fake News Detection Web App** that uses **Machine Learning** to classify news articles as _Fake_ or _Real_.

Built with:

- 🧐 Python + Scikit-learn (Model Training)
- 🧪 Flask (Backend API)
- ⚛️ React.js (Frontend UI)
- 📊 TF-IDF Vectorizer + Logistic Regression

---

## 📌 Features

✅ Paste a news article and get instant prediction  
✅ Clean and responsive UI  
✅ React + Flask integration  
✅ Trained on real Fake/True datasets  
✅ Easily extendable to other models (e.g., Naive Bayes, SVM)

---

## 📁 Project Structure

```
project-root/
│
├── archive/                # Raw dataset files (Fake.csv, True.csv)
│
├── backend/                # Flask backend
│   ├── app.py              # Flask server
│   ├── model.pkl           # Trained ML model
│   └── vectorizer.pkl      # Saved TF-IDF vectorizer
│
├── fake-news/              # React frontend
│   ├── src/
│   │   └── components/
│   │       └── Fake_news_UI.js
│   └── App.js, index.js, etc.
```

---

## 🧠 Machine Learning Model

- **Dataset**: Merged from `Fake.csv` and `True.csv` (from Kaggle)
- **Text Preprocessing**: Tokenization, stopword removal, lowercasing
- **Vectorization**: TF-IDF
- **Classifier**: Logistic Regression (also tested Naive Bayes)
- **Accuracy**: ~93% on validation data

---

## 🚀 How to Run Locally

### 🔧 Backend (Flask API)

```bash
cd backend
pip install flask scikit-learn joblib
python app.py
```

It will run on: `http://127.0.0.1:5000`

---

### ⚛️ Frontend (React App)

```bash
cd fake-news
npm install
npm start
```

Open `http://localhost:3000` in your browser.

---

## 📤 API Endpoint

**POST** `/predict`  
**Request Body**:

```json
{ "text": "your news article here..." }
```

**Response**:

```json
{ "prediction": "Fake" }
```

---

## 🗄️ UI Preview

(Add a screenshot here of your app once running)

---

## 📚 Future Improvements

- Use BERT or LSTM for deeper language understanding
- Add source URL credibility checker
- Save prediction history
- User authentication

---

## 📜 License

This project is for educational purposes.

---

## 🙋‍♀️ Made with ❤️ by Mamta Gupta
