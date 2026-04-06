from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# -------- LOAD DATA FIRST --------
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
    return random.choice(quotes) if quotes else "No quotes available"


# -------- ROUTES --------
@app.route("/")
def home():
    quote = get_random_quote()
    return render_template("index.html", quote=quote)


@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "quotesops"
    })


@app.route("/api")
def api():
    quote = get_random_quote()
    return jsonify({"quote": quote})


# -------- RUN APP --------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)