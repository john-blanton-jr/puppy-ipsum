from flask import Flask, render_template, jsonify, request
from utils.generator import generate_paragraph
from dotenv import load_dotenv
import requests
import os

app = Flask(__name__)

load_dotenv()

api_key = os.environ.get("API_KEY")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/display_text")
def display_text():
    return render_template("display.html")


@app.route("/generate_ipsum")
def generate_ipsum():
    try:
        num_paragraphs = int(request.args.get("numParagraphs", 1))
        start_with = request.args.get("startWith", "false").lower() == "true"

        paragraphs = [generate_paragraph() for _ in range(num_paragraphs)]

        generated_text = "\n\n".join(paragraphs)

        if start_with:
            paragraphs[0] = "Puppy Ipsum " + paragraphs[0]
        generated_text = "\n\n".join(paragraphs)

        return jsonify(text=generated_text)
    except Exception as e:
        return jsonify(error=str(e)), 500


@app.route("/get_puppy_image")
def get_puppy_image():
    try:
        response = requests.get(
            "https://api.pexels.com/v1/search?query=puppy&per_page=80",
            headers={"Authorization": api_key},
        )
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify(error=str(e)), 500


if __name__ == "__main__":
    app.run(debug=True)
