from flask import Flask, render_template
from scraper import get_trends

app = Flask(__name__)

@app.route("/")
def home():

    trends = get_trends()

    return render_template("index.html", trends=trends)

app.run(host="0.0.0.0", port=5000)
