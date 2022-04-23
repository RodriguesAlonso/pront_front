from flask import Flask

from pront_front.ext import site
from pront_front.ext import config
from pront_front.ext import database


def create_app():

    app = Flask(__name__)
    config.init_app(app)
    database.init_app(app)
    site.init_app(app)
    return app
