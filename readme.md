# 🤖 GemBot Pro

GemBot Pro is a modern AI chatbot built with **Streamlit** and powered by **Google Gemini AI**. It provides a clean dark-themed chat interface, conversation history, quick suggestions, and real-time AI responses.

---

## ✨ Features

- 🚀 Powered by Google Gemini 2.5 Flash
- 💬 Interactive Chat Interface
- 🎨 Modern Dark UI Design
- 🧠 Conversation Memory
- ⚡ Fast Response Generation
- 📊 Conversation Turn Counter
- 🗑 Clear Chat Functionality
- 💡 Predefined Suggestion Buttons
- 🔒 Secure API Key Management using `.env`

---

## 📸 Preview

### Home Screen
- Modern dark-themed interface
- AI-powered assistant
- Suggested prompts for quick interaction

### Chat Screen
- User and AI chat bubbles
- Message timestamps
- Persistent conversation history

---

## 🛠 Technologies Used

- Python 3.10+
- Streamlit
- Google Generative AI (Gemini)
- python-dotenv

---

## 📂 Project Structure

```text
GemBot-Pro/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## 🚀 Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/GemBot-Pro.git
cd GemBot-Pro
```

### 2. Create Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Get Gemini API Key

1. Visit Google AI Studio:
   https://aistudio.google.com/

2. Create an API Key.

3. Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

---

## ▶ Running the Application

```bash
streamlit run app.py
```

Application will start at:

```text
http://localhost:8501
```

---

## ⚙ Configuration

You can customize these values inside `app.py`:

```python
MODEL_NAME = "gemini-2.5-flash"
TEMPERATURE = 0.7
MAX_TOKENS = 1024
```

### Temperature

| Value | Behavior |
|---------|----------|
| 0.2 | More factual |
| 0.5 | Balanced |
| 0.7 | Creative |
| 1.0 | Highly creative |

---

## 🎯 Example Prompts

- Explain Artificial Intelligence
- What is Cloud Computing?
- Write a Python Fibonacci Program
- Explain Machine Learning Simply
- Generate a professional email
- Create a project roadmap

---

## 🔒 Security

Never upload your `.env` file to GitHub.

Add this to `.gitignore`:

```gitignore
.env
__pycache__/
venv/
```

---

## 📦 requirements.txt

```txt
streamlit
google-generativeai
python-dotenv
```

---

## 🖥 Deployment

### Streamlit Community Cloud

1. Push project to GitHub.
2. Login to:
   https://share.streamlit.io/
3. Create a new app.
4. Select repository.
5. Add:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

inside Streamlit Secrets.

6. Deploy.

---

## Future Improvements

- 🌐 Multi-language Support
- 📁 File Uploads
- 🎤 Voice Input
- 🔊 Text-to-Speech
- 📄 Chat Export (PDF)
- 🌙 Light/Dark Theme Toggle
- 🧠 Long-Term Memory
- 📊 Analytics Dashboard

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Prashanth**

## Website Link

****

Built with ❤️ using Streamlit and Google Gemini AI.
