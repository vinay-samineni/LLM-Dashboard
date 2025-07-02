# 🧠 LLaMA-Powered NLP Web Service with Flask

This project hosts a locally loaded [Meta LLaMA 3.2-1B](https://huggingface.co/meta-llama/Llama-3.2-1B) model on a Flask server to provide three powerful natural language processing services:

- ✍️ **Text Generation**
- 💬 **Sentiment Analysis**
- 📄 **Text Summarization**

The project offers a basic frontend through an HTML interface and RESTful API endpoints to interact with the models.

---

## 🚀 Features

- 🦙 Local hosting of LLaMA-3.2-1B for natural text generation
- 🔍 Real-time sentiment analysis via Hugging Face's pipeline
- 📝 Abstractive summarization using custom prompts
- ⚡ Flask-based backend with a minimal HTML frontend
- 🔌 JSON-based API endpoints for easy integration

---

## 🏗️ Project Structure

llama-nlp-app/
├── app.py # Flask server and route definitions
├── templates/
│ └── index.html # Frontend interface (basic UI)
├── static/ # Optional: CSS/JS assets (not required for basic setup)
└── README.md # Project documentation


---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/llama-nlp-app.git
cd llama-nlp-app

**2. Create a Virtual Environment**
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

**3. Install Dependencies**
pip install torch transformers flask


⚙️ Usage
**1. Start the Flask Server**
python app.py

**2. API Endpoints**
➤ /generate (POST)
Generates text using the LLaMA model.

Request Body:
{
  "prompt": "Once upon a time"
}

Response:
{
  "response": "Once upon a time, there was a..."
}

➤ /sentiment (POST)
Returns sentiment classification (e.g., POSITIVE, NEGATIVE).
Request Body:
{
  "text": "I love using AI!"
}

Response:
{
  "sentiment": "POSITIVE"
}

➤ /summarize (POST)
Summarizes long text input.
Request Body:
{
  "text": "In a recent development, scientists discovered that..."
}

Response:
{
  "summary": "Scientists made a new discovery..."
}

🧠 Models Used

meta-llama/Llama-3.2-1B – for generation and summarization
Hugging Face default sentiment pipeline – for sentiment analysis
Make sure you have the LLaMA model downloaded and available locally or access via Hugging Face with a valid token if needed.

🛡️ Requirements

Python 3.8+
CUDA-enabled GPU (Recommended but not mandatory)
Internet access (for downloading models initially)

🖼️ Frontend
A simple HTML file (index.html) is served at / to interact with the APIs via a web UI. You can customize this as needed.


---

Let me know if you’d also like a matching `requirements.txt` or a sample `index.html` to go with this!
