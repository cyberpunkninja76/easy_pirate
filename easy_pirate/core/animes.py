import requests
from bs4 import BeautifulSoup
import cloudscraper
import re


ROOT_HOME = "https://www.animefreak.tv/home/"
ROOT_WATCH = "https://www.animefreak.tv/watch/"


def __getAllAnimes():
    url = f"{ROOT_HOME}anime-list/"
    response = requests.get(url)
    page = response.content
    soup = BeautifulSoup(page, "html.parser")
    animes = []
    div = soup.find("div", {"class": "container-left"})
    for ul in div.find_all("ul", {"class": "arrow-list"}):
        for li in ul.find_all("li"):
            for a in li.find_all("a"):
                urlTitle = a["href"][len(ROOT_WATCH):]
                animes.append({"url": a["href"],
                               "urlTitle": urlTitle,
                               "title": a.text})
    return animes


def searchAnAnime(title):
    matchingAnimes = []
    for anime in __getAllAnimes():
        if title.lower() in anime["title"].lower():
            matchingAnimes.append(anime)
    return matchingAnimes


def __getPageURL(urlTitle, episode, isDubs):
    pageURL = f"{ROOT_WATCH}{urlTitle}/episode/episode-{episode}/"
    if isDubs:
        pageURL += "/2/"
    return pageURL


def getVideoURL(urlTitle, episode, isDubs):
    pageURL = __getPageURL(urlTitle, episode, isDubs)
    session = cloudscraper.create_scraper()
    response = session.get(pageURL)
    for match in re.finditer(r"file\s*:\s*[\"\']\s*([htps][^\"\']+)",
                             response.text):
        if "mp4" in match.group(1):
            return match.group(1)
    return None
