from easy_pirate import app
from flask import render_template


@app.route("/")
def animes():
    return render_template("animes.html")
