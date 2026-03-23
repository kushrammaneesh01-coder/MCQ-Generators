# 🦜⛓️ MCQs Creator Application with LangChain

An AI-powered Multiple Choice Question (MCQ) generator built with **LangChain**, **OpenAI GPT-3.5 Turbo**, and **Streamlit**. Upload any PDF or text file and instantly generate customized MCQs with automated complexity review.

---

## 🚀 Features

- 📄 Upload **PDF** or **TXT** files as source material
- 🔢 Generate **3 to 50 MCQs** in one click
- 🎯 Specify **subject** and **complexity level**
- 🤖 Powered by **OpenAI GPT-3.5 Turbo** via LangChain
- 📊 Auto **quiz evaluation** and review by a second LLM chain
- 🖥️ Clean **Streamlit** web interface

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| LLM | OpenAI GPT-3.5 Turbo |
| Orchestration | LangChain (LLMChain + SequentialChain) |
| Frontend | Streamlit |
| File Parsing | PyPDF2 |
| Config | python-dotenv |

---

## 📁 Project Structure

```
MCQ-Generators/
├── StreamlitApp.py          # Main Streamlit application
├── Response.json            # JSON template for MCQ response format
├── requirements.txt         # Python dependencies
├── setup.py                 # Local package setup
├── .env                     # Environment variables (API Key)
└── src/
    └── mcqgenerator/
        ├── MCQGenrator.py   # LangChain chains (quiz generation + evaluation)
        ├── utils.py         # File reading & table formatting utilities
        └── logger.py        # Logging configuration
```

---

## ✅ Prerequisites

Make sure you have the following installed before starting:

- **Python 3.8 or higher** — [Download Python](https://www.python.org/downloads/)
- **pip** (comes with Python)
- An **OpenAI API Key** — [Get one here](https://platform.openai.com/api-keys)

---

## 📦 Step-by-Step Setup & Run Guide

### Step 1: Clone or Download the Project

If using Git:
```bash
git clone https://github.com/your-username/MCQ-Generators.git
cd MCQ-Generators
```

Or simply **download and extract** the ZIP and open a terminal inside the folder.

---

### Step 2: Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

> You should see `(venv)` appear at the start of your terminal prompt.

---

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs all required packages including:
- `openai`, `langchain`, `langchain-openai`, `langchain-community`
- `streamlit`, `python-dotenv`, `PyPDF2`, `pandas`

> The `-e .` line in `requirements.txt` also installs the local `mcqgenerator` package (from `src/`) in editable mode.

---

### Step 4: Set Up Your OpenAI API Key

Create a `.env` file in the root of the project (if it doesn't exist):

```
OPENAI_API_KEY=your_openai_api_key_here
```

> ⚠️ **Never share your API key publicly or commit it to GitHub.**

---

### Step 5: Run the Application

```bash
streamlit run StreamlitApp.py
```

The app will automatically open in your browser at:
```
http://localhost:8501
```

---

## 🖥️ How to Use the App

1. **Upload File** — Click "Browse files" and upload a `.pdf` or `.txt` file (your study material)
2. **Set MCQ Count** — Choose the number of questions (between 3 and 50)
3. **Enter Subject** — Type the subject name (e.g., `Science`, `History`, `Python`)
4. **Set Complexity** — Enter the difficulty level (e.g., `Simple`, `Medium`, `Hard`)
5. **Click "Create MCQs"** — Wait for the AI to generate and review your questions
6. **View Results** — A table of MCQs and an AI review will appear below

---

## ⚠️ Troubleshooting

| Problem | Solution |
|---|---|
| `ModuleNotFoundError: No module named 'mcqgenrator'` | Run `pip install -e .` in the project root |
| `openai.AuthenticationError` | Check your `OPENAI_API_KEY` in the `.env` file |
| `streamlit: command not found` | Run `pip install streamlit` |
| `PyPDF2` errors on PDF upload | Ensure the PDF is not password-protected |
| App not opening in browser | Manually visit `http://localhost:8501` |

---

## 👤 Author

**Maneesh Kushram**
- Email: kushrammaneesh01@gmail.com

---

## 📄 License

This project is licensed under the terms of the [LICENSE](LICENSE) file included in this repository.