from flask import Flask
from ext import views

app = Flask(__name__)
views.init_app(app)
app.run()
    