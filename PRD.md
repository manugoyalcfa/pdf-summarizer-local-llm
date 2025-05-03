# 🧾 PDF Summarizer with Local LLM – Product Requirements Document (PRD)

## Overview
The PDF Summarizer is a lightweight tool for offline use that allows users to upload a PDF and get a high-level summary using a locally hosted Large Language Model (LLM). It’s designed for personal use and privacy-first workflows.

---

## Problem Statement
Users often need quick insights from lengthy PDFs but either lack internet access or prefer not to send documents to cloud services. Existing solutions are either expensive, require uploads, or are not privacy-conscious.

---

## Goals
- Extract text from PDFs locally
- Summarize it using an LLM running offline
- Provide a simple, easy-to-use interface
- Run on standard consumer hardware (Ryzen 7, 32 GB RAM)

---

## Target Users
- Students and researchers
- Knowledge workers
- Tech enthusiasts learning LLMs

---

## Features (MVP)
- PDF upload via UI
- Text extraction using PyMuPDF
- Summarization via LLaMA 3.2 (local, via Ollama)
- Basic Streamlit web interface

---

## Out of Scope
- Multi-file uploads
- Cloud integration
- Full document indexing or search

---

## Future Enhancements
- Chunk-based summarization for large files
- Save summaries to local disk
- Allow summarization by section or page
- Select among multiple local models
