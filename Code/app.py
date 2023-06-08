"""Main script, uses other modules to generate sentences."""
from flask import Flask
from weighted import weighted_sample



app = Flask(__name__)


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    sentence = weighted_sample()
    return f"<p>{sentence}</p>"


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
