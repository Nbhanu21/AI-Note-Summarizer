from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>AI-Powered Smart Note Summarizer</h1>
    <p>Welcome to our AI learning platform.</p>
    <p>Day 1 - Flask application is working!</p>
    """


if __name__ == "__main__":
    app.run(debug=True)