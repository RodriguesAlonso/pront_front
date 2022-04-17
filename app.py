from flask import Flask, render_template
from ext import views
from ext import database
#from ext import database

app = Flask(__name__)
views.init_app(app)
database.init_app(app)

