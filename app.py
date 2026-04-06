from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

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

# Root → HTML page
@app.route("/")
def home():
    return render_template("index.html")

# API endpoint → JSON response
@app.route("/api")
def api():
    quote = get_random_quote()
    return jsonify({"quote": quote})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "quotesops"
    }), 200