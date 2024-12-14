# 🧠✨ AI Math Notes App

An AI-powered math notes application that leverages the **Gemini API** to help provide AI responses for hand drawn notes. Built with **React** and **TypeScript** for the frontend and a **Python** backend to handle AI processing.

---

## 🚀 Features

- 📝 **Smart Notes**: Automatically generate sample AI responses for
- 🔍 **Problem Solver**: Input math problems and receive solutions.
- ⚡ **Fast Backend**: Python backend with FastAPI, integrating the Gemini API.

---

## 📦 Tech Stack

- **Frontend**: React, TypeScript, Tailwind CSS
- **Backend**: Python, FastAPI
- **AI API**: Gemini API
- **Package Management**: npm, pip

---

## 🛠️ Installation

### Prerequisites

- **Node.js**: [Download here](https://nodejs.org/)
- **Python** (>=3.8): [Download here](https://www.python.org/)
- **Gemini API Key**: [Get it here](https://ai.google.dev/)

### Clone the Repository

```bash
git clone https://github.com/yourusername/ai-math-notes-app.git
cd caiculator
```

### Frontend Setup

```bash
cd caiculator
npm install
npm run dev
```

The frontend will be available at `http://localhost:3000`.

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python main.py
```

The backend will run at `http://localhost:8900`.

---

## ⚙️ Environment Variables

Create a `.env` file in the `backend` directory and add your Gemini API key:

```plaintext
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## 📄 Folder Structure

```
ai-math-notes-app/
├── frontend/            # React + TypeScript frontend
│   ├── src/
│   │   ├── components/  # Reusable React components
│   │   ├── screens/       # Application pages
│   │   └── App.tsx      # Main React component
│   └── package.json
├── backend/             # Python + FastAPI backend
│   ├── main.py           # Main backend script
│   └── requirements.txt # Backend dependencies
└── README.md
```



## 🌟 Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit: `git commit -m "Add new feature"`.
4. Push the branch: `git push origin feature-branch`.
5. Open a pull request.


Happy coding! 🧠✨
