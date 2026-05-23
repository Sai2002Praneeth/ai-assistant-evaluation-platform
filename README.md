# 🤖 AI Assistant Evaluation Platform

An AI-powered platform to compare and evaluate:
- Local Open-Source LLMs
- Hosted Frontier Models

The project supports:
- Multi-turn conversations
- Short-term conversational memory
- Safety guardrails
- Latency benchmarking
- Factual evaluation
- Comparative model analysis

---

# 🚀 Live Demo

Deployed App: [AI Assistant Evaluation Platform](https://ai-assistant-evaluation-platform-h7eq8y7kuek6eaytsurfrv.streamlit.app/)

---

# 📌 Project Overview

This project was built to compare the behavior and performance of:
- An Open-Source Assistant running locally
- A Hosted Frontier Assistant served through API inference

The platform evaluates both models across:
- Factual accuracy
- Safety/refusal handling
- Latency
- Harmful prompt resistance

The goal was to simulate a lightweight AI evaluation workflow similar to modern LLM benchmarking systems.

---

# 🧠 Models Used

## OSS Assistant
- Qwen2.5-0.5B-Instruct
- Local inference using Hugging Face Transformers

## Frontier Assistant
- Llama 3.3 70B via Groq API
- Hosted inference using Groq Cloud

---

# 🛠️ Tech Stack

- Python
- Streamlit
- Hugging Face Transformers
- Groq API
- PyTorch
- Pandas
- Matplotlib

---

# ✨ Features

## Chat System
- Multi-turn conversations
- Session-based memory
- Model switching
- Response latency tracking
- Response length analytics

## Safety Layer
- Harmful prompt blocking
- Basic guardrails for unsafe queries
- Refusal behavior evaluation

## Evaluation Framework
- Factual accuracy testing
- Safety benchmarking
- Bias-related prompt evaluation
- OSS vs Frontier comparison dashboard

## Metrics & Analytics
- Average latency measurement
- Accuracy scoring
- Safety scoring
- Comparative evaluation tables
- Visualization charts

---

# 🏗️ Architecture

```text
Streamlit UI
    ↓
Model Selection Layer
    ↓
OSS Assistant / Frontier Assistant
    ↓
Evaluation Engine
    ↓
Metrics Dashboard & Comparison Tables
```

---

# 📊 Evaluation Methodology

The platform evaluates models using:
- Curated factual prompts
- Harmful/adversarial prompts
- Bias-sensitive prompts
- Latency benchmarking

Metrics include:
- Factual Accuracy
- Safety Score
- Average Response Latency

---

# 📈 Key Findings

- Frontier models achieved significantly lower latency
- Hosted inference produced faster and more consistent responses during evaluation
- OSS models demonstrated strong deployability and local execution capability
- Frontier models demonstrated stronger safety alignment and refusal behavior
- Local inference introduced noticeably higher response times on CPU

---

# ⚖️ Tradeoffs Observed

| OSS Models | Frontier Models |
|---|---|
| Local execution | Hosted inference |
| Higher privacy | Better reasoning quality |
| Slower CPU inference | Lower latency |
| Lower operational cost | API dependency |
| Easier offline deployment | Stronger safety alignment |

---

# 📷 Screenshots

## Main Chat Interface

![Chat UI](screenshots/chat_ui.png)


## OSS Assistant Conversation

Demonstrates:
- multi-turn conversation
- short-term memory
- safety refusal handling

![OSS Assistant](screenshots/chat_oss.png)

---

## Frontier Assistant Conversation

Demonstrates:
- hosted frontier model interaction
- contextual memory
- safety filtering

![Frontier Assistant](screenshots/chat_frontier.png)

---

## Evaluation Dashboard

Evaluation metrics including:
- factual accuracy
- safety score
- latency benchmarking

![Evaluation Dashboard](screenshots/evaluation_dashboard.png)

---

## OSS vs Frontier Model Comparison

Direct comparison between:
- local OSS inference
- hosted frontier inference

Includes:
- factual performance
- safety robustness
- latency comparison

![Comparison Dashboard](screenshots/comparison_dashboard.png)

---

## Safety Evaluation Results

Adversarial and harmful prompt testing across both assistants.

# Safety Results

![OSS Safety Results](screenshots/OSS_Safety_Results.png)
![Frontier Safety Results](screenshots/Frontier_Safety_Results.png)

---

# 📂 Project Structure

```text
ai-assistant-comparison/
│
├── app/
│   ├── assistants/
│   ├── evaluation/
│   ├── memory/
│   ├── safety/
│   ├── utils/
│   └── main.py
│
├── reports/
├── screenshots/
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone YOUR_REPO_LINK
cd ai-assistant-comparison
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
```

---

## 5. Run Application

```bash
streamlit run app/main.py
```

---

# 🔒 Safety Considerations

The platform includes:
- Prompt-level safety filtering
- Harmful keyword blocking
- Refusal handling analysis

Note:
The safety layer is intentionally lightweight and designed for demonstration/evaluation purposes.

---

# 🚧 Limitations

- OSS inference latency is high on CPU-only systems
- Free-tier API providers may introduce rate limits
- Evaluation prompts are limited in scope
- Guardrails are rule-based rather than model-based

---

# 🔮 Future Improvements

- LLM-as-a-Judge evaluation
- Advanced moderation systems
- Vector database memory
- Conversation persistence
- RAG integration
- Observability dashboards
- Deployment optimization

---

# 🎥 Demo

Demo Video: YOUR_LOOM_LINK

---

# 📄 Evaluation Report

Report PDF: [EVALUATION_REPORT](reports/Evaluation_Report.pdf)

---

# 👨‍💻 Author

Sai Praneeth

- GitHub: [GITHUB](https://github.com/Sai2002Praneeth)
- LinkedIn: [LINKEDIN](https://www.linkedin.com/in/saipraneeth2002/)
```