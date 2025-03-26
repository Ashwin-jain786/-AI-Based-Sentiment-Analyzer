from flask import Flask, request, jsonify, render_template
from sentiment_analysis import analyze_sentiment
from db_operations import Database

app = Flask(__name__)
db = Database()  # Initialize the database connection

@app.route("/")
def home():
    return render_template("index.html")  # Serve the HTML file

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    result = analyze_sentiment(data["text"])
    db.insert_review(data["text"], result)  # Store the review in the database
    return jsonify(result)

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)
