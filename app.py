from flask import Flask, jsonify
import random

app = Flask(__name__)

# Load quotes once
def load_quotes():
    try:
        with open("quotes.txt", "r") as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print("Error reading quotes file:", e)
        return []

quotes = load_quotes()

if not quotes:
    print("No quotes found in quotes.txt")


def get_random_quote():
    return random.choice(quotes)


# Home route
@app.route("/")
def home():
    return "QuotesOps is running 🚀"


# Health check route
@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "quotesops"
    })


# API endpoint
@app.route("/api")
def api():
    quote = get_random_quote()
    return jsonify({"quote": quote})


# 🔥 ONLY ONE app.run
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)