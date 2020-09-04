from flask import Flask

app = Flask(__name__)

from easy_pirate.views import view
