from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# Home route (your UI)
@app.route("/")
def home():
    return "QuotesOps is running 🚀"

# Health check route
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "service": "quotesops"
    }), 200

# IMPORTANT: host must be 0.0.0.0 for Docker
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

# Load quotes once (like Java static load)
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

# Get random quote (like your Java method)
def get_random_quote():
    return random.choice(quotes)


# API endpoint → JSON response
@app.route("/api")
def api():
    quote = get_random_quote()
    return jsonify({"quote": quote})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

