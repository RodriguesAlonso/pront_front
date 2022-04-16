from flask import Flask
from ext import views

app = Flask(__name__)

if __name__ == '__main__':
    views.init_app(app)
    app.run()
    