from flask import Flask, render_template, request, jsonify
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Initialize Flask app
app = Flask(__name__)

# Load LLaMA model for text generation
model_name = "meta-llama/Llama-3.2-1B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to("cuda" if torch.cuda.is_available() else "cpu")

# Load sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

@app.route("/")
def index():
    return render_template("index.html")  # Serve UI

@app.route("/generate", methods=["POST"])
def generate_text():
    """ Generates text using LLaMA model """
    try:
        data = request.json
        user_input = data.get("prompt", "")

        if not user_input:
            return jsonify({"response": "Please enter a prompt."})

        # Tokenize input and generate response
        inputs = tokenizer(user_input, return_tensors="pt").to(model.device)
        output_ids = model.generate(
            **inputs, 
            max_length=100,  # Adjust length
            temperature=0.7, 
            top_p=0.9,
            do_sample=True
        )
        generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

        return jsonify({"response": generated_text})

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/sentiment", methods=["POST"])
def analyze_sentiment():
    """ Performs sentiment analysis on user input """
    try:
        data = request.json
        user_input = data.get("text", "")

        if not user_input:
            return jsonify({"sentiment": "Please enter a text to analyze."})

        # Get sentiment prediction
        result = sentiment_analyzer(user_input)[0]
        sentiment = result["label"]

        return jsonify({"sentiment": sentiment})

    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route("/summarize", methods=["POST"])
def summarize_text():
    """Summarizes text using your LLaMA model."""
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"summary": "Please provide text for summarization."})

    prompt = f"Summarize the following text accurately:\n\n{text}\n\nSummary:"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    summary_ids = model.generate(
        **inputs,
        max_length=150,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.2,
        do_sample=True
    )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return jsonify({"summary": summary})


if __name__ == "__main__":
    app.run(debug=True)
