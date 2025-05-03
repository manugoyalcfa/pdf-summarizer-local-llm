# 🧾 PDF Summarizer with Local LLM

This is a simple personal project that allows you to upload a PDF file and generate a summary using a locally running LLM (e.g., LLaMA 3) via [Ollama](https://ollama.com). The app is built with Python and Streamlit and runs entirely offline.

---

## 🛠️ Tech Stack

- Python 3.10+
- Streamlit (UI)
- PyMuPDF (PDF text extraction)
- Ollama (to run LLM locally)
- LLaMA 3 (7B model)

---

## 📦 Setup Instructions

### 1. Install dependencies

```bash
pip install streamlit pymupdf
```

### 2. Pull the LLaMA 3 model

```bash
ollama pull llama3
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## 📁 File Structure

- `app.py`: Streamlit web app interface
- `summarize.py`: Extracts text from PDF
- `README.md`: Documentation (this file)

---

## 🧠 How It Works

1. You upload a PDF via the web interface.
2. The app extracts text using PyMuPDF.
3. The first 3000 characters are sent as a prompt to the local LLaMA 3 model.
4. A summary is displayed.

---

## ✨ Future Enhancements

- Support multi-page summarization
- Save summary to file
- Option to summarize by section or paragraph
- Add smaller model support (e.g., Mistral, Phi)

---

## 🔐 Disclaimer

This is a personal learning project and is not intended for production use.
