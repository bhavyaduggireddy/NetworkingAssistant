# 🤝 Personalized Networking Assistant

An AI-powered web application that helps users prepare for professional networking events by analyzing event details, generating networking conversation topics, verifying factual statements, and maintaining interaction history. The application is built using FastAPI, Streamlit, and Google's Gemini AI.

---

## 🚀 Features

- 🤖 AI Event Analysis
- 💬 Networking Topic Generator
- 🔍 AI Fact Checker
- ⭐ User Feedback Collection
- 📜 Conversation History
- 📝 Feedback History
- ⚡ REST API with FastAPI
- 🎨 Interactive Streamlit User Interface
- ✅ Automated Testing using Pytest and Mocking

---

## 🛠️ Technologies Used

- Python
- FastAPI
- Streamlit
- Google Gemini API
- Pydantic
- Requests
- Pytest
- Pytest-Mock
- Uvicorn
- Python-dotenv

---

## 📂 Project Structure

```
NetworkingAssistant/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│
├── tests/
│   └── test_event_analyzer.py
│
├── streamlit_app.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/NetworkingAssistant.git
```

### 2. Navigate to the project

```bash
cd NetworkingAssistant
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Create a .env file

```text
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Running the Backend

```bash
uvicorn main:app --reload
```

Backend runs at

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## ▶️ Running the Frontend

```bash
streamlit run streamlit_app.py
```

Streamlit runs at

```
http://localhost:8501
```

---

## 🧪 Running Tests

```bash
pytest
```

All tests pass using mocked Gemini API responses.

---

## 📸 Screenshots

Add screenshots of:

- Home Page
- AI Event Analysis
- Fact Checker
- Conversation History
- Feedback Section

---

## 📌 Future Improvements

- User Authentication
- MongoDB Integration
- Export Analysis to PDF
- Event Recommendations
- Cloud Deployment

---

## 👨‍💻 Author

**Bhavya Duggireddy**