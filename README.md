---
title: Qwen OSS Assistant
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: streamlit
app_file: app/main.py
pinned: false
---

# Qwen OSS Assistant

Public deployment of an Open-Source AI Assistant using Qwen2.5-0.5B-Instruct.

---

## Live Deployment

Hugging Face Space:  
https://huggingface.co/spaces/Codeszz/qwen-oss-assistant

---

## Overview

This project demonstrates a lightweight Open-Source AI assistant deployed publicly using Hugging Face Spaces.

The assistant supports:

- Multi-turn conversations
- Short-term conversational memory
- Basic assistant-like interactions
- Public inference through Streamlit UI

The deployment was built as part of an AI assistant evaluation and benchmarking project.

---

## Model Used

### Open-Source Model

- Qwen/Qwen2.5-0.5B-Instruct

Inference is performed locally using Hugging Face Transformers.

---

## Features

- Public OSS deployment
- Streamlit chat interface
- Lightweight CPU inference
- Conversational context handling
- Safety-aware assistant behavior
- Hugging Face Spaces deployment

---

## Tech Stack

- Python
- Streamlit
- Hugging Face Transformers
- PyTorch
- Hugging Face Spaces

---

## Project Structure

```text
app/
│
├── assistants/
│   └── oss_assistant.py
│
└── main.py
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Sai2002Praneeth/ai-assistant-evaluation-platform
cd ai-assistant-evaluation-platform
```

---

### Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run Application

```bash
streamlit run app/main.py
```

---

## Deployment Notes

The OSS assistant is deployed publicly using Hugging Face Spaces with Streamlit.

The deployment uses:

- CPU-based inference
- Hugging Face Transformers
- Qwen2.5-0.5B-Instruct

This deployment demonstrates:

- public OSS model hosting
- lightweight inference workflows
- deployability of open-source LLMs

---

## Limitations

- CPU inference latency is higher than hosted frontier APIs
- Small OSS models have weaker reasoning quality compared to larger hosted models
- Memory is session-based and temporary
- No persistent storage or vector database implemented

---

## Future Improvements

- GPU deployment optimization
- Persistent conversational memory
- Better prompt engineering
- Advanced safety moderation
- Quantized inference optimization
- Retrieval-Augmented Generation (RAG)

---

## Author

Sai Praneeth

GitHub:  
https://github.com/Sai2002Praneeth

LinkedIn:  
https://www.linkedin.com/in/saipraneeth2002/
