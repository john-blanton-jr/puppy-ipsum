from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    Response,
    render_template_string,
)
from utils.generator import generate_paragraph
from dotenv import load_dotenv
import requests
import os
import datetime

application = Flask(__name__)

load_dotenv()

api_key = os.environ.get("API_KEY")


@application.route("/")
def home():
    return render_template("index.html")


@application.route("/display_text")
def display_text():
    return render_template("display.html")


@application.route("/generate_ipsum")
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


@application.route("/get_puppy_image")
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


def generate_sitemap(app):
    sitemap_template = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    {% for route in routes %}
    <url>
        <loc>{{ url_root }}{{ route }}</loc>
        <lastmod>{{ lastmod }}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    {% endfor %}
</urlset>
    """
    routes = []
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and len(rule.arguments) == 0:
            url = f"{rule.rule}"
            routes.append(url)

    sitemap_xml = render_template_string(
        sitemap_template,
        routes=routes,
        lastmod=datetime.datetime.now().date(),
        url_root=request.url_root,
    )
    return sitemap_xml


@application.route("/sitemap.xml")
def sitemap():
    sitemap_xml = generate_sitemap(application)
    return Response(sitemap_xml, mimetype="application/xml")


if __name__ == "__main__":
    application.run()
