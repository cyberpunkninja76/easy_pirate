from easy_pirate import app
from easy_pirate.core.animes import searchAnAnime, getVideoURL
from flask import render_template, request


@app.route("/", methods=["GET", "POST"])
@app.route("/animes/", methods=["GET", "POST"])
def animes():
    animeTitle = ""
    if request.method == "POST":
        animeTitle = request.form["animeTitle"]
    return render_template("animes.html",
                           title="Select an anime!",
                           matchingAnimes=searchAnAnime(animeTitle))


@app.route("/animes/<urlTitle>/<episode>/<language>/")
def watch(urlTitle, episode, language):
    videoURL = getVideoURL(urlTitle=urlTitle,
                           episode=int(episode),
                           isDubs=(language == "Dubs"))
    return render_template("watch.html", title=urlTitle, videoURL=videoURL)
