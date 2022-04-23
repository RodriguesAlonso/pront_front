from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Usuario(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(140), nullable=False)
    date_create = db.Column(db.DateTime, default=datetime.utcnow)
	#dataNacimento = db.Column(db.DateTime)
	#login = db.Column(db.String(20), unique=True)
	#senha = db.Column(db.String(20))
	#paciente_id = db.Column(db.Integer, db.ForeignKey('paciente_id'))
    def __repr__(self):
        return '<Nome %r>' % self.id
''' 
class Medico(db.Model, SerializerMixin):
	id = db.Column(db.Integer, primary_key=True)
	crm = db.Column(db.String(10), unique=True)
	nome = db.Column(db.String(140), unique=True)
	#id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
	
class Pacientes(db.Model, SerializerMixin):
	id = db.Column(db.Integer, primary_key=True)
	CartSus = db.Column(db.String(20), unique=True)
	#histFam = db.Column(db.String(300))
	histPac = db.Column(db.Text())
	#nome = db.relationship('Usuario', backref='paciente', lazy=True)
'''