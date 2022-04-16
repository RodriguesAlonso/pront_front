from flask import Flask, render_template
from ext import views

app = Flask(__name__)
views.init_app(app)

if __name__ == '__main__':
    app.run(port=5000)