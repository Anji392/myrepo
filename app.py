from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is a Flask app!"

@app.route("/about")
def about():
    return "This is the about page."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

