# app.py
from flask import Flask, request, render_template
from aitextgen import aitextgen

MAX_LENGTH = 64
TEMPERATURE = 0.95

trained_ai = aitextgen(model_folder="trained_model")
trained_ai.generate_one(max_length=MAX_LENGTH, temperature=TEMPERATURE)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def display_lyrics():
    new_lyrics = trained_ai.generate_one(max_length=MAX_LENGTH, temperature=TEMPERATURE)
    return render_template("display.html", generated_lyrics=new_lyrics)

if __name__ == "__main__":
    app.run(threaded=True, port=8080)