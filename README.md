# MindEase 🧠

MindEase is an AI-powered mood reflection web app designed for students. It allows users to log daily moods with short reflections, then analyzes the reflections using sentiment analysis to provide weekly insights and gentle suggestions for emotional awareness.

## 🚩 Problem
Many students experience stress and emotional ups-and-downs, but lack simple tools to reflect on and understand their feelings over time.

## 💡 Solution
MindEase helps users:
- Log daily feelings and reflections
- Automatically analyze sentiment (Positive / Neutral / Negative)
- View summary insights for the last 7 days
- Receive supportive suggestions based on trends

> **Note:** MindEase focuses on awareness and reflection — it does *not* diagnose medical conditions.

## ⚙️ Tech Stack
- **Backend:** Django (Python)
- **Database:** SQLite
- **AI/NLP:** TextBlob sentiment analysis
- **Frontend:** Django templates (HTML + CSS)


## 🚀 How to Run Locally

1. Clone the repo  
   ```bash
   git clone https://github.com/AbhinavGupta-code/mindease.git
````

2. Create a virtual environment

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Run migrations

   ```bash
   python manage.py migrate
   ```

4. Start the server

   ```bash
   python manage.py runserver
   ```

5. Open in browser
   `http://127.0.0.1:8000/`

---

## 🔮 Future Improvements

* Add visual data charts
* User authentication
* Reminder notifications
* Mobile UI optimization

---
