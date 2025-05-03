import streamlit as st
import subprocess
from summarize import extract_text_from_pdf

def run_llm_summary(text):
    prompt = f"Summarize the following PDF content:\n\n{text[:3000]}"  # Keep it under limit
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt.encode(),
        stdout=subprocess.PIPE
    )
    return result.stdout.decode("utf-8")

st.set_page_config(page_title="PDF Summarizer", layout="centered")
st.title("📄 PDF Summarizer with Local LLM")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    st.info("Extracting text...")
    text = extract_text_from_pdf(uploaded_file)
    st.success("Text extracted. Ready to summarize.")

    if st.button("Summarize"):
        with st.spinner("Summarizing..."):
            summary = run_llm_summary(text)
        st.subheader("🧾 Summary:")
        st.write(summary)
