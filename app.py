from flask import Flask
from ext import views

app = Flask(__name__)
views.init_app(app)

if __name__ == '__main__':
    app.run()
    