from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

'''
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://cowqxsowfwmzxg:abebd323848c44cba1fa2c7c508e4771bed17524adc8f629ac34ceadca8d0ec3@ec2-34-197-84-74.compute-1.amazonaws.com:5432/dauskq533vma6p'

'''
def init_app(app):
    db = SQLAlchemy(app)
